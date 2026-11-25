const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber()', function () {
  it('Sums correctly two integers.', function () {
    assert.strictEqual(calculateNumber(2, 3), 5);
  });

  it('Rounds correctly the first number.', function () {
    assert.strictEqual(calculateNumber(2.25, 3), 5);
  });

  it('Rounds correctly the second number.', function () {
    assert.strictEqual(calculateNumber(2, 3.25), 5);
  });

  it('Rounds correctly both numbers.', function () {
    assert.strictEqual(calculateNumber(-2, -3), -5);
  });
});
