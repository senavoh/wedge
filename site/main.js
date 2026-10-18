/* ==========================================================
   WEDGE SITE CONFIG — change the repo / commands here only.
   (The HTML hrefs carry the same values as a no-JS fallback;
   a find-and-replace of "senavoh/wedge" updates everything.)
   ========================================================== */
const WEDGE = {
  repo: "senavoh/wedge",
  github: "https://github.com/senavoh/wedge",
  domain: "getwedge.dev",
  cmd: {
    npx: "npx skills add senavoh/wedge",
    skill: (name) => `npx skills add senavoh/wedge --skill ${name}`,
    pluginAdd: "/plugin marketplace add senavoh/wedge",
    pluginInstall: "/plugin install wedge@wedge",
    curl: "curl -fsSL https://getwedge.dev/install.sh | sh",
    clone: "git clone https://github.com/senavoh/wedge",
    manualCopy: "cp -r wedge/skills/* ~/.claude/skills/",
  },
  usage: "Use wedge to find me a business I can start with $500 and 10 hours a week.",
};

const SKILLS = [
  { name: "wedge", cat: "core", desc: "Runs the whole pipeline end to end, keeps state, verifies, renders the report." },
  { name: "wedge-niche-scout", cat: "research", desc: "Mines “I wish there was”, “alternative to” and “too expensive” posts to find niches with unmet demand that fit you." },
  { name: "wedge-competitor-map", cat: "research", desc: "Real pricing, positioning and a feature matrix for every competitor, all cited." },
  { name: "wedge-review-miner", cat: "research", desc: "Turns hundreds of 1–3 star reviews and complaint threads into ranked pain themes with exact quotes." },
  { name: "wedge-gap-ranker", cat: "strategy", desc: "Scores opportunities on six axes with reasoning shown, then a separate critic pass tries to kill the winner. GO / PIVOT / KILL." },
  { name: "wedge-win-plan", cat: "strategy", desc: "Switching triggers, positioning in customers’ own words, offers that win switchers, where unhappy customers hang out, comparison page and outreach drafts." },
  { name: "wedge-launch-kit", cat: "launch", desc: "Name with a verified-available domain, pricing anchored to competitors, cheapest stack, landing page, and a 7-day validation test with a pass bar and kill criteria." },
  { name: "wedge-watch", cat: "launch", desc: "Monthly re-check: new complaints, price changes, new entrants, fresh switching triggers." },
];

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- fill config values ---------- */
document.querySelectorAll("[data-cmd]").forEach((el) => {
  const v = WEDGE.cmd[el.dataset.cmd];
  if (typeof v === "string") el.textContent = v;
});
document.querySelectorAll("[data-usage]").forEach((el) => (el.textContent = `“${WEDGE.usage}”`));
document.querySelectorAll("[data-gh]").forEach((el) => (el.href = WEDGE.github));
document.querySelectorAll("[data-gh-issues]").forEach((el) => (el.href = WEDGE.github + "/issues"));
document.querySelectorAll("[data-domain]").forEach((el) => (el.textContent = WEDGE.domain));

/* ---------- skill catalog ---------- */
const list = document.querySelector("[data-skills]");
const more = document.querySelector("[data-more]");
const PREVIEW = 4; // cards shown under "All" before "Show all"
let expanded = false;
if (list) {
  const label = { core: "Core", research: "Research", strategy: "Strategy", launch: "Launch" };
  SKILLS.forEach((s) => {
    const li = document.createElement("li");
    li.className = "skill";
    li.dataset.cat = s.cat;
    const cmd = WEDGE.cmd.skill(s.name);
    li.innerHTML = `
      <div class="skill__top"><h3></h3><span class="skill__cat">${label[s.cat]}</span></div>
      <p></p>
      <div class="skill__copy"><code></code><button class="copy" type="button"><span>Copy</span></button></div>`;
    li.querySelector("h3").textContent = s.name;
    li.querySelector("p").textContent = s.desc;
    li.querySelector("code").textContent = cmd;
    const btn = li.querySelector(".copy");
    btn.dataset.copyText = cmd;
    btn.setAttribute("aria-label", `Copy install command for ${s.name}`);
    list.appendChild(li);
  });

  const tabs = document.querySelectorAll("[data-filter] button");
  const status = document.querySelector("[data-filter-status]");
  const apply = (cat) => {
    let n = 0;
    list.querySelectorAll(".skill").forEach((card, i) => {
      const match = cat === "all" || card.dataset.cat === cat;
      const show = match && (cat !== "all" || expanded || i < PREVIEW);
      card.hidden = !show;
      if (show) n++;
    });
    if (more) more.parentElement.hidden = cat !== "all" || expanded;
    if (status) status.textContent = `Showing ${n} skill${n === 1 ? "" : "s"}`;
  };
  tabs.forEach((t) =>
    t.addEventListener("click", () => {
      tabs.forEach((x) => x.setAttribute("aria-pressed", String(x === t)));
      apply(t.dataset.cat);
    })
  );
  if (more) more.addEventListener("click", () => { expanded = true; apply("all"); });
  apply("all");
}

/* ---------- copy buttons ---------- */
const live = document.createElement("div");
live.className = "sr-only";
live.setAttribute("aria-live", "polite");
document.body.appendChild(live);

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    let ok = false;
    try { ok = document.execCommand("copy"); } catch { ok = false; }
    ta.remove();
    return ok;
  }
}

document.addEventListener("click", async (e) => {
  const btn = e.target.closest(".copy");
  if (!btn) return;
  const text = btn.dataset.copyText || WEDGE.cmd[btn.dataset.copyFrom];
  if (!text) return;
  const ok = await copyText(text);
  const lbl = btn.querySelector("span") || btn;
  lbl.textContent = ok ? "Copied" : "Press ⌘C";
  btn.classList.toggle("is-done", ok);
  live.textContent = ok ? "Copied to clipboard" : "Copy failed, select the text manually";
  clearTimeout(btn._t);
  btn._t = setTimeout(() => {
    lbl.textContent = "Copy";
    btn.classList.remove("is-done");
  }, 1800);
});

/* ---------- install tabs (ARIA tabs pattern) ---------- */
const tablist = document.querySelector('.itabs [role="tablist"]');
if (tablist) {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const select = (tab, focus) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
    if (focus) tab.focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => select(t));
    t.addEventListener("keydown", (e) => {
      let j = null;
      if (e.key === "ArrowRight") j = (i + 1) % tabs.length;
      if (e.key === "ArrowLeft") j = (i - 1 + tabs.length) % tabs.length;
      if (e.key === "Home") j = 0;
      if (e.key === "End") j = tabs.length - 1;
      if (j !== null) { e.preventDefault(); select(tabs[j], true); }
    });
  });
}

/* ---------- nav border on scroll ---------- */
const nav = document.querySelector(".nav");
const onScroll = () => nav && nav.classList.toggle("is-scrolled", window.scrollY > 8);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

/* ---------- scroll reveal ---------- */
if (!reduceMotion) {
  const els = document.querySelectorAll(".block .head, .vs, .runs, .block .split > *, .quotes, .points, .modes, .steps, .skills, .report, .wins, .itabs, .faq, .support");
  els.forEach((el) => el.classList.add("reveal"));
  // Reveal anything whose top has entered the lower edge of the viewport, including
  // anything already scrolled past (fast jumps and anchor links).
  const sweep = () => {
    const edge = window.innerHeight * 0.92;
    document.querySelectorAll(".reveal:not(.is-in)").forEach((el) => {
      if (el.getBoundingClientRect().top < edge) el.classList.add("is-in");
    });
  };
  let queued = false;
  const queue = () => { if (!queued) { queued = true; requestAnimationFrame(() => { queued = false; sweep(); }); } };
  ["scroll", "resize", "hashchange", "load"].forEach((ev) => window.addEventListener(ev, queue, { passive: true }));
  sweep();
}

/* ---------- live star count (shows only once the repo is public) ---------- */
fetch(`https://api.github.com/repos/${WEDGE.repo}`, { headers: { Accept: "application/vnd.github+json" } })
  .then((r) => (r.ok ? r.json() : null))
  .then((d) => {
    if (!d || typeof d.stargazers_count !== "number" || d.stargazers_count < 1) return;
    const n = d.stargazers_count;
    const txt = n >= 1000 ? (n / 1000).toFixed(n >= 10000 ? 0 : 1).replace(/\.0$/, "") + "k" : String(n);
    document.querySelectorAll("[data-stars]").forEach((el) => {
      el.textContent = "★ " + txt;
      el.closest(".gh")?.classList.add("has-count");
    });
  })
  .catch(() => {});
