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

        sinon.assert.calledOnce(spy);
        sinon.assert.calledWith(spy, 'SUM', 100, 20);
    });
});
