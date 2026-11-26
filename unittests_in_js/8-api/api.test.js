const { expect } = require('chai');
const request = require('request');

describe('Index Page', function () {
    it('Returns 200 status code.', function (done) {
        const result = request('http://localhost:7865/', function (error, response, body) {
            if (error) {
                return done(error);
            }

            try {
                expect(response.statusCode).to.equal(200);
                done();
            } catch (error) {
                done(error);
            }
        });
    });

    it('Returns correct content.', function (done) {
        const result = request('http://localhost:7865/', function (error, response, body) {
            if (error) {
                return done(error);
            }

            try {
                expect(body).to.equal('Welcome to the payment system');
                done();
            } catch (error) {
                done(error);
            }
        });
    });
});
