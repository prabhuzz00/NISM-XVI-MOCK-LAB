const SET_META = [
  { id: 1, title: "Set 1", blurb: "Foundation paper: markets, futures pricing, options payoffs and hedging." },
  { id: 2, title: "Set 2", blurb: "Indices, spreads, tick/margin maths and trading mechanism." },
  { id: 3, title: "Set 3", blurb: "Clearing, settlement, risk, options strategies and legal framework." },
  { id: 4, title: "Set 4", blurb: "Accounting, taxation, investor protection and mixed numericals." },
  { id: 5, title: "Set 5", blurb: "Full-syllabus revision paper with extra application numericals." }
];

const REAL_META = [
  { id: 1, title: "Real Set 1", blurb: "50 questions transcribed from the first sample recording." },
  { id: 2, title: "Real Set 2", blurb: "50 questions transcribed from the second sample recording." },
  { id: 3, title: "Real Set 3", blurb: "Questions transcribed from the third sample recording." },
  { id: 4, title: "Real Set 4", blurb: "50 questions transcribed from the fourth sample recording." },
  { id: 5, title: "Real Set 5", blurb: "50 questions transcribed from the fifth sample recording." }
];

const REAL_BANKS = {
  1: () => window.SET_01_VIDEO,
  2: () => window.SET_02_VIDEO,
  3: () => window.SET_03_VIDEO,
  4: () => window.SET_04_VIDEO,
  5: () => window.SET_05_VIDEO
};

const MOCK_DURATION_SEC = 120 * 60;
const REAL_DURATION_SEC = 60 * 60;
const PASS_RATIO = 0.6;

const state = {
  view: "home",
  mode: "mock",
  setId: null,
  questions: [],
  answers: [],
  current: 0,
  remaining: MOCK_DURATION_SEC,
  duration: MOCK_DURATION_SEC,
  passMark: 60,
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
    <article class="card set-card" data-mode="mock" data-set="${s.id}">
      <h3>${s.title}</h3>
      <p>${s.blurb}</p>
      <div class="set-meta"><span>100 MCQs</span><span>Start mock →</span></div>
    </article>
  `).join("");
  $("realGrid").innerHTML = REAL_META.map(s => {
    const count = (REAL_BANKS[s.id]() || []).length;
    return `
      <article class="card set-card" data-mode="real" data-set="${s.id}">
        <h3>${s.title}</h3>
        <p>${s.blurb}</p>
        <div class="set-meta"><span>${count} MCQs · 60 min</span><span>Start →</span></div>
      </article>
    `;
  }).join("");
  document.querySelectorAll(".set-card").forEach(el => {
    el.addEventListener("click", () => startSet(el.dataset.mode, Number(el.dataset.set)));
  });
}

function startSet(mode, setId) {
  const bank = mode === "real"
    ? ((REAL_BANKS[setId] && REAL_BANKS[setId]()) || [])
    : ((window.QUESTION_SETS && window.QUESTION_SETS[setId]) || []);
  const expected = mode === "real" ? 1 : 100;
  if (bank.length < expected || (mode === "mock" && bank.length !== 100)) {
    alert("Question bank is still loading or incomplete. Please refresh once.");
    return;
  }
  state.mode = mode;
  state.setId = setId;
  state.duration = mode === "real" ? REAL_DURATION_SEC : MOCK_DURATION_SEC;
  state.passMark = +(bank.length * PASS_RATIO).toFixed(2);
  state.questions = bank.map(q => ({ ...q }));
  state.answers = Array(bank.length).fill(null);
  state.current = 0;
  state.remaining = state.duration;
  state.submitted = false;
  if (state.timerId) clearInterval(state.timerId);
  state.timerId = setInterval(tick, 1000);
  $("homeView").classList.add("hidden");
  $("resultView").classList.add("hidden");
  $("examView").classList.remove("hidden");
  $("submitBtn").style.display = "";
  $("examSet").textContent = mode === "real" ? `Real ${setId}` : setId;
  $("examTotal").textContent = bank.length;
  $("examTimer").textContent = formatTime(state.duration);
  $("examTimer").classList.remove("warn", "danger");
  $("headerActions").innerHTML = `<button class="btn-ghost" id="quitBtn">Back to sets</button>`;
  $("quitBtn").onclick = () => {
    if (confirm("Leave this test? Progress for this attempt will be lost.")) {
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
      <p>${q.explanation || ""}</p>
      ${q.example ? `<p><strong>Example:</strong> ${q.example}</p>` : ""}
    </div>`;

  const kicker = q.chapter
    ? `Chapter ${q.chapter}: ${q.chapterName} · ${q.topic}`
    : (state.mode === "real" ? `Real QNA · Set ${state.setId}` : "");
  const last = state.questions.length - 1;

  $("questionCard").innerHTML = `
    ${kicker ? `<div class="q-kicker">${kicker}</div>` : ""}
    <p class="question">${q.q}</p>
    <div class="options">${optionsHtml}</div>
    ${explain}
    <div class="nav">
      <button class="btn-ghost" id="prevBtn" ${i === 0 ? "disabled" : ""}>Previous</button>
      <button class="btn-primary" id="nextBtn">${i === last ? "Review last question" : "Next"}</button>
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
  $("nextBtn").onclick = () => {
    if (state.current < state.questions.length - 1) { state.current++; renderQuestion(); }
  };
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
  const total = state.questions.length;
  const score = +(correct * 1 + wrong * -0.25).toFixed(2);
  const passed = score >= state.passMark;

  const byChapter = {};
  state.questions.forEach((q, i) => {
    const key = `${q.chapter}. ${q.chapterName}`;
    if (!byChapter[key]) byChapter[key] = { total: 0, correct: 0, wrong: 0, na: 0 };
    byChapter[key].total++;
    if (state.answers[i] == null) byChapter[key].na++;
    else if (state.answers[i] === q.answer) byChapter[key].correct++;
    else byChapter[key].wrong++;
  });

  const hasChapters = state.questions.some(q => q.chapter);
  const rows = Object.entries(byChapter).map(([name, s]) => {
    const chScore = +(s.correct - 0.25 * s.wrong).toFixed(2);
    return `<tr><td>${name}</td><td>${s.total}</td><td>${s.correct}</td><td>${s.wrong}</td><td>${s.na}</td><td>${chScore}</td></tr>`;
  }).join("");
  const chapterTable = hasChapters ? `
      <table class="chapter-table">
        <thead><tr><th>Chapter</th><th>Qs</th><th>Right</th><th>Wrong</th><th>NA</th><th>Net</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>` : "";
  const paperName = state.mode === "real" ? `Real QNA Set ${state.setId}` : `Set ${state.setId}`;

  $("examView").classList.add("hidden");
  $("resultView").classList.remove("hidden");
  $("resultView").innerHTML = `
    <div class="result-card">
      <div class="${passed ? "pass" : "fail"}">${passed ? "PASS" : "FAIL"}</div>
      <div class="score-big">${score}</div>
      <p>${paperName}. Scoring: +1 for correct, −0.25 for wrong, 0 for unanswered. Pass mark ${state.passMark} / ${total}.</p>
      <div class="score-grid">
        <div><b>${correct}</b><span>Correct × 1 = ${correct.toFixed(2)}</span></div>
        <div><b>${wrong}</b><span>Wrong × −0.25 = ${(wrong * -0.25).toFixed(2)}</span></div>
        <div><b>${unanswered}</b><span>Unanswered × 0 = 0.00</span></div>
        <div><b>${score}</b><span>Net score / ${total}</span></div>
      </div>
      ${chapterTable}
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
  const optionCount = state.questions[state.current] ? state.questions[state.current].options.length : 0;
  if (idx != null && idx < optionCount && state.answers[state.current] == null) {
    state.answers[state.current] = idx;
    renderQuestion();
  } else if (e.key === "n" || e.key === "ArrowRight") {
    if (state.current < state.questions.length - 1) { state.current++; renderQuestion(); }
  } else if (e.key === "p" || e.key === "ArrowLeft") {
    if (state.current > 0) { state.current--; renderQuestion(); }
  }
});

renderHome();
