const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber()', function () {
  describe('Sum', function () {
    it('Sums correctly two integers.', function () {
      expect(calculateNumber('SUM', 2, 3)).to.equal(5);
    });

    it('Rounds correctly the first number before summing.', function () {
      expect(calculateNumber('SUM', 2.25, 3)).to.equal(5);
    });

    it('Rounds correctly the second number before summing.', function () {
      expect(calculateNumber('SUM', 2, 3.25)).to.equal(5);
    });

    it('Rounds correctly both numbers before summing.', function () {
      expect(calculateNumber('SUM', -2, -3)).to.equal(-5);
    });
  });

  describe('Subtract', function () {
    it('Subtracts correctly two integers.', function () {
      expect(calculateNumber('SUBSTRACT', 2, 3)).to.equal(-1);
    });

    it('Rounds correctly the first number before subtracting.', function () {
      expect(calculateNumber('SUBTRACT', 2.25, 3)).to.equal(-1);
    });

    it('Rounds correctly the second number before subtracting.', function () {
      expect(calculateNumber('SUBTRACT', 2, 3.25)).to.equal(-1);
    });

    it('Rounds correctly both numbers before subtracting.', function () {
      expect(calculateNumber('SUBTRACT', -2, -3)).to.equal(1);
    });
  });

  describe('Divide', function () {
    it('Divides correctly two integers.', function () {
      expect(calculateNumber('DIVIDE', 9, 3)).to.equal(3);
    });

    it('Rounds correctly the first number before dividing.', function () {
      expect(calculateNumber('DIVIDE', 9.25, 3)).to.equal(3);
    });

    it('Rounds correctly the second number before dividing.', function () {
      expect(calculateNumber('DIVIDE', 9, 3.25)).to.equal(3);
    });

    it('Rounds correctly both numbers before dividing.', function () {
      expect(calculateNumber('DIVIDE', -9, -3)).to.equal(3);
    });

    it('Raises an error when trying to divide by zero.', function () {
      expect(calculateNumber('DIVIDE', -9, 0)).to.equal('Error');
    });

    it('Rounds correctly the second number before checking it\'s not zero.', function () {
      expect(calculateNumber('DIVIDE', -9, 0.25)).to.equal('Error');
    });
  });
});
