const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi()', function () {
    let stubCalculateNumber;
    let spyConsoleLog;

    beforeEach(function () {
        stubCalculateNumber = sinon.stub(Utils, 'calculateNumber').returns(10);
        spyConsoleLog = sinon.spy(console, 'log');
    });

    afterEach(function () {
        stubCalculateNumber.restore();
        spyConsoleLog.restore();
    });

    it('Calls Utils.calculateNumber() with the right arguments.', function () {
        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnceWithExactly(stubCalculateNumber, 'SUM', 100, 20);
    });

    it('Logs the output correctly.', function () {
        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnceWithExactly(spyConsoleLog, 'The total is: 10');
    });
});
