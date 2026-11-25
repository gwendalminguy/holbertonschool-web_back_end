const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi()', function () {
    let spy;

    beforeEach(function () {
        spy = sinon.spy(Utils, 'calculateNumber');      // Set up a spy.
    });

    afterEach(function () {
        spy.restore();
    });

    it('Function sendPaymentRequestToApi() calls Utils.calculateNumber() with the right arguments.', function () {
        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnce).to.be.true;
        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(spy.returned(120)).to.be.true;
    });
});
