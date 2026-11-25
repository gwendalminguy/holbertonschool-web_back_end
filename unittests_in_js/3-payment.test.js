const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi()', function () {
    let spy;
    let logStub;

    beforeEach(function () {
        spy = sinon.spy(Utils, 'calculateNumber');      // Set up a spy.
        logStub = sinon.stub(console, 'log');           // Silence console.log()
    });

    afterEach(function () {
        spy.restore();
        logStub.restore();
    });

    it('Function sendPaymentRequestToApi() calls Utils.calculateNumber() with the right arguments.', function () {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    });
});
