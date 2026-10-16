// Crock Math engine - slow cooker conversion, fill band and serving honesty.
// Every norm is a labeled kitchen norm; the app never judges doneness or food safety.

function assertPositive(value, label) {
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(label + " must be above zero");
  }
}

function tenths(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function fixed1(x) {
  return tenths(x).toFixed(1);
}

// Labeled norm: every 30 minutes of oven simmering becomes about 2 hours on high or 4.5 on low.
function convertTruth(ovenMinutes) {
  assertPositive(ovenMinutes, "the oven time");
  const high = tenths(ovenMinutes / 30 * 2);
  const low = tenths(ovenMinutes / 30 * 4.5);
  return ovenMinutes + " oven minutes becomes about " + fixed1(high) + " hours on high or " +
    fixed1(low) + " hours on low honestly.";
}

// Labeled norm: a slow cooker works best half to three-quarters full.
function fillTruth(loadQuarts, cookerQuarts) {
  assertPositive(loadQuarts, "the load");
  assertPositive(cookerQuarts, "the cooker");
  const f = tenths(loadQuarts / cookerQuarts);
  let band;
  if (f > 1) {
    band = "more stew than the cooker holds";
  } else if (f < 0.5) {
    band = "under half full, so it runs hot and fast - check it early";
  } else if (f <= 0.7) {
    band = "right in the half-to-three-quarter band";
  } else {
    band = "past three-quarters, so it runs slow and crowds the lid";
  }
  return fixed1(loadQuarts) + " quarts of stew in " + article(cookerQuarts) + " " + fixed1(cookerQuarts) +
    "-quart cooker fills it " + fixed1(f) + " of the way, " + band + " honestly.";
}

function article(n) {
  const s = String(Math.abs(Math.trunc(n)));
  return (/^([8]|11|18)/.test(s)) ? "an" : "a";
}

// Labeled norm: a serving of stew is about 1.5 cups.
function servingTruth(servings) {
  assertPositive(servings, "the serving count");
  const cups = tenths(servings * 1.5);
  const quarts = tenths(cups / 4);
  const word = servings === 1 ? "serving" : "servings";
  return servings + " " + word + " " + (servings === 1 ? "asks" : "ask") + " " + fixed1(cups) +
    " cups, " + fixed1(quarts) + " quarts, of stew honestly.";
}

if (typeof module !== "undefined") {
  module.exports = { convertTruth, fillTruth, servingTruth, tenths, fixed1 };
}
