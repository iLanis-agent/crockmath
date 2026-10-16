const engine = require("./engine.js");
const cases = require("./expected.json");

let failed = 0;
let checks = 0;

for (const c of cases) {
  checks++;
  let got;
  try {
    got = { result: engine[c.fn](...c.args) };
  } catch (e) {
    got = { error: e.message };
  }
  const want = "result" in c ? { result: c.result } : { error: c.error };
  if (JSON.stringify(got) !== JSON.stringify(want)) {
    failed++;
    console.log("FAIL", c.fn, JSON.stringify(c.args));
    console.log("  want:", JSON.stringify(want));
    console.log("  got: ", JSON.stringify(got));
  }
}

console.log(`${cases.length} cases / ${checks} checks, ${failed} failed`);
process.exit(failed === 0 ? 0 : 1);
