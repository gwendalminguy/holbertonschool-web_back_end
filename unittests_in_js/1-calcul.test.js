const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber()', function () {
  describe('Sum', function () {
    it('Sums correctly two integers.', function () {
      assert.strictEqual(calculateNumber('SUM', 2, 3), 5);
    });

    it('Rounds correctly the first number before summing.', function () {
      assert.strictEqual(calculateNumber('SUM', 2.25, 3), 5);
    });

    it('Rounds correctly the second number before summing.', function () {
      assert.strictEqual(calculateNumber('SUM', 2, 3.25), 5);
    });

    it('Rounds correctly both numbers before summing.', function () {
      assert.strictEqual(calculateNumber('SUM', -2, -3), -5);
    });
  });

  describe('Subtract', function () {
    it('Subtracts correctly two integers.', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2, 3), -1);
    });

    it('Rounds correctly the first number before subtracting.', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.25, 3), -1);
    });

    it('Rounds correctly the second number before subtracting.', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2, 3.25), -1);
    });

    it('Rounds correctly both numbers before subtracting.', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', -2, -3), 1);
    });
  });

  describe('Divide', function () {
    it('Divides correctly two integers.', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 9, 3), 3);
    });

    it('Rounds correctly the first number before dividing.', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 9.25, 3), 3);
    });

    it('Rounds correctly the second number before dividing.', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 9, 3.25), 3);
    });

    it('Rounds correctly both numbers before dividing.', function () {
      assert.strictEqual(calculateNumber('DIVIDE', -9, -3), 3);
    });

    it('Raises an error when trying to divide by zero.', function () {
      assert.strictEqual(calculateNumber('DIVIDE', -9, 0), 'Error');
    });

    it('Rounds correctly the second number before checking it\'s not zero.', function () {
      assert.strictEqual(calculateNumber('DIVIDE', -9, 0.25), 'Error');
    });
  });
});
