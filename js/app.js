const SET_META = [
  { id: 1, title: "Set 1", blurb: "Foundation paper: markets, futures pricing, options payoffs and hedging." },
  { id: 2, title: "Set 2", blurb: "Indices, spreads, tick/margin maths and trading mechanism." },
  { id: 3, title: "Set 3", blurb: "Clearing, settlement, risk, options strategies and legal framework." },
  { id: 4, title: "Set 4", blurb: "Accounting, taxation, investor protection and mixed numericals." },
  { id: 5, title: "Set 5", blurb: "Full-syllabus revision paper with extra application numericals." }
];

const DURATION_SEC = 120 * 60;
const PASS_MARK = 60;

const state = {
  view: "home",
  setId: null,
  questions: [],
  answers: [],
  current: 0,
  remaining: DURATION_SEC,
  timerId: null,
  submitted: false
};

function $(id) { return document.getElementById(id); }

function formatTime(sec) {
  const h = Math.floor(sec / 3600);
  const m = Math.floor((sec % 3600) / 60);
  const s = sec % 60;
  return [h, m, s].map(n => String(n).padStart(2, "0")).join(":");
}

function renderHome() {
  $("homeView").classList.remove("hidden");
  $("examView").classList.add("hidden");
  $("resultView").classList.add("hidden");
  $("headerActions").innerHTML = "";
  $("setGrid").innerHTML = SET_META.map(s => `
    <article class="card set-card" data-set="${s.id}">
      <h3>${s.title}</h3>
      <p>${s.blurb}</p>
      <div class="set-meta"><span>100 MCQs</span><span>Start mock →</span></div>
    </article>
  `).join("");
  document.querySelectorAll(".set-card").forEach(el => {
    el.addEventListener("click", () => startSet(Number(el.dataset.set)));
  });
}

function startSet(setId) {
  const bank = (window.QUESTION_SETS && window.QUESTION_SETS[setId]) || [];
  if (bank.length !== 100) {
    alert("Question bank is still loading or incomplete. Please refresh once.");
    return;
  }
  state.setId = setId;
  state.questions = bank.map(q => ({ ...q }));
  state.answers = Array(100).fill(null);
  state.current = 0;
  state.remaining = DURATION_SEC;
  state.submitted = false;
  if (state.timerId) clearInterval(state.timerId);
  state.timerId = setInterval(tick, 1000);
  $("homeView").classList.add("hidden");
  $("resultView").classList.add("hidden");
  $("examView").classList.remove("hidden");
  $("submitBtn").style.display = "";
  $("examSet").textContent = setId;
  $("headerActions").innerHTML = `<button class="btn-ghost" id="quitBtn">Back to sets</button>`;
  $("quitBtn").onclick = () => {
    if (confirm("Leave this mock test? Progress for this attempt will be lost.")) {
      clearInterval(state.timerId);
      renderHome();
    }
  };
  buildMap();
  renderQuestion();
}

function tick() {
  state.remaining -= 1;
  const el = $("examTimer");
  el.textContent = formatTime(Math.max(0, state.remaining));
  el.classList.toggle("warn", state.remaining <= 15 * 60);
  el.classList.toggle("danger", state.remaining <= 5 * 60);
  if (state.remaining <= 0) submitTest(true);
}

function buildMap() {
  $("qMap").innerHTML = state.questions.map((_, i) =>
    `<button type="button" data-i="${i}">${i + 1}</button>`
  ).join("");
  $("qMap").onclick = (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    state.current = Number(btn.dataset.i);
    renderQuestion();
  };
}

function paletteClass(i) {
  if (i === state.current) return "current";
  const ans = state.answers[i];
  if (ans == null) return "";
  return ans === state.questions[i].answer ? "right" : "wrong";
}

function renderQuestion() {
  const i = state.current;
  const q = state.questions[i];
  const chosen = state.answers[i];
  $("examQNo").textContent = i + 1;
  [...$("qMap").children].forEach((btn, idx) => {
    btn.className = paletteClass(idx);
  });

  const optionsHtml = q.options.map((opt, idx) => {
    let cls = "option";
    if (chosen != null) {
      if (idx === q.answer) cls += " correct";
      else if (idx === chosen && chosen !== q.answer) cls += " wrong";
    }
    return `<button class="${cls}" data-idx="${idx}" ${chosen != null ? "disabled" : ""}>
      <span class="key">${String.fromCharCode(65 + idx)}</span>${opt}
    </button>`;
  }).join("");

  const explain = chosen == null ? "" : `
    <div class="explain">
      <h4>${chosen === q.answer ? "Correct" : "Incorrect"} — why this is the answer</h4>
      <p>${q.explanation}</p>
      ${q.example ? `<p><strong>Example:</strong> ${q.example}</p>` : ""}
    </div>`;

  $("questionCard").innerHTML = `
    <div class="q-kicker">Chapter ${q.chapter}: ${q.chapterName} · ${q.topic}</div>
    <p class="question">${q.q}</p>
    <div class="options">${optionsHtml}</div>
    ${explain}
    <div class="nav">
      <button class="btn-ghost" id="prevBtn" ${i === 0 ? "disabled" : ""}>Previous</button>
      <button class="btn-primary" id="nextBtn">${i === 99 ? "Review last question" : "Next"}</button>
    </div>
  `;

  $("questionCard").querySelectorAll(".option").forEach(btn => {
    btn.addEventListener("click", () => {
      if (state.answers[i] != null) return;
      state.answers[i] = Number(btn.dataset.idx);
      renderQuestion();
    });
  });
  $("prevBtn").onclick = () => { if (state.current > 0) { state.current--; renderQuestion(); } };
  $("nextBtn").onclick = () => { if (state.current < 99) { state.current++; renderQuestion(); } };
  const box = $("questionCard").querySelector(".explain");
  if (box) box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

$("submitBtn").addEventListener("click", () => submitTest(false));

function submitTest(auto) {
  if (state.submitted) return;
  const unanswered = state.answers.filter(a => a == null).length;
  if (!auto && unanswered && !confirm(`You have ${unanswered} unanswered question(s). Unanswered questions score 0. Submit now?`)) {
    return;
  }
  state.submitted = true;
  clearInterval(state.timerId);
  const correct = state.answers.filter((a, i) => a === state.questions[i].answer).length;
  const wrong = state.answers.filter((a, i) => a != null && a !== state.questions[i].answer).length;
  const score = +(correct * 1 + wrong * -0.25).toFixed(2);
  const passed = score >= PASS_MARK;

  const byChapter = {};
  state.questions.forEach((q, i) => {
    const key = `${q.chapter}. ${q.chapterName}`;
    if (!byChapter[key]) byChapter[key] = { total: 0, correct: 0, wrong: 0, na: 0 };
    byChapter[key].total++;
    if (state.answers[i] == null) byChapter[key].na++;
    else if (state.answers[i] === q.answer) byChapter[key].correct++;
    else byChapter[key].wrong++;
  });

  const rows = Object.entries(byChapter).map(([name, s]) => {
    const chScore = +(s.correct - 0.25 * s.wrong).toFixed(2);
    return `<tr><td>${name}</td><td>${s.total}</td><td>${s.correct}</td><td>${s.wrong}</td><td>${s.na}</td><td>${chScore}</td></tr>`;
  }).join("");

  $("examView").classList.add("hidden");
  $("resultView").classList.remove("hidden");
  $("resultView").innerHTML = `
    <div class="result-card">
      <div class="${passed ? "pass" : "fail"}">${passed ? "PASS" : "FAIL"}</div>
      <div class="score-big">${score}</div>
      <p>NISM scoring: +1 for correct, −0.25 for wrong, 0 for unanswered. Pass mark 60/100.</p>
      <div class="score-grid">
        <div><b>${correct}</b><span>Correct × 1 = ${correct.toFixed(2)}</span></div>
        <div><b>${wrong}</b><span>Wrong × −0.25 = ${(wrong * -0.25).toFixed(2)}</span></div>
        <div><b>${unanswered}</b><span>Unanswered × 0 = 0.00</span></div>
        <div><b>${score}</b><span>Net score / 100</span></div>
      </div>
      <table class="chapter-table">
        <thead><tr><th>Chapter</th><th>Qs</th><th>Right</th><th>Wrong</th><th>NA</th><th>Net</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <div class="nav" style="justify-content:center;margin-top:18px">
        <button class="btn-primary" id="reviewBtn">Review answers</button>
        <button class="btn-ghost" id="homeBtn">Choose another set</button>
      </div>
    </div>
  `;
  $("homeBtn").onclick = renderHome;
  $("reviewBtn").onclick = () => {
    $("resultView").classList.add("hidden");
    $("examView").classList.remove("hidden");
    $("submitBtn").style.display = "none";
    renderQuestion();
  };
}

document.addEventListener("keydown", (e) => {
  if ($("examView").classList.contains("hidden")) return;
  if (["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;
  const map = { "1": 0, "2": 1, "3": 2, "4": 3, a: 0, b: 1, c: 2, d: 3 };
  const idx = map[e.key.toLowerCase()];
  if (idx != null && state.answers[state.current] == null) {
    state.answers[state.current] = idx;
    renderQuestion();
  } else if (e.key === "n" || e.key === "ArrowRight") {
    if (state.current < 99) { state.current++; renderQuestion(); }
  } else if (e.key === "p" || e.key === "ArrowLeft") {
    if (state.current > 0) { state.current--; renderQuestion(); }
  }
});

renderHome();
