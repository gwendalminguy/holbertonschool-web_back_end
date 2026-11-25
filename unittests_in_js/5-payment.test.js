const sinon = require('sinon');

const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi()', function () {
    let spyConsoleLog;

    beforeEach(function () {
        spyConsoleLog = sinon.spy(console, 'log');
    });

    afterEach(function () {
        spyConsoleLog.restore();
    });

    it('Logs the output correctly by calling console.log() once (120).', function () {
        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnceWithExactly(spyConsoleLog, 'The total is: 120');
    });

    it('Logs the output correctly by calling console.log() once (20).', function () {
        sendPaymentRequestToApi(10, 10);

        sinon.assert.calledOnceWithExactly(spyConsoleLog, 'The total is: 20');
    });
});
