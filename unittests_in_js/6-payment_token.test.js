const { expect } = require('chai');

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI()', function () {
    it('Calling getPaymentTokenFromAPI(false) does nothing.', function () {
        const result = getPaymentTokenFromAPI(false);

        expect(result).to.equal(undefined);
    });

    it('Calling getPaymentTokenFromAPI(true) returns a resolved promise.', function (done) {
        getPaymentTokenFromAPI(true)
            .then((result) => {
                expect(result.data).to.equal('Successful response from the API');
                done();
            })
            .catch(done);
    });
});
