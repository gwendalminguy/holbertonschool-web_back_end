const { expect } = require('chai');
const request = require('request');

describe('Express Application', function () {
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

    describe('Cart Page', function () {
        it('Returns 200 status code on valid ID.', function (done) {
            const result = request('http://localhost:7865/cart/666', function (error, response, body) {
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

        it('Returns correct content on valid ID.', function (done) {
            const result = request('http://localhost:7865/cart/666', function (error, response, body) {
                if (error) {
                    return done(error);
                }

                try {
                    expect(body).to.equal('Payment methods for cart 666');
                    done();
                } catch (error) {
                    done(error);
                }
            });
        });

        it('Returns 404 status code on invalid ID.', function (done) {
            const result = request('http://localhost:7865/cart/hello', function (error, response, body) {
                if (error) {
                    return done(error);
                }

                try {
                    expect(response.statusCode).to.equal(404);
                    done();
                } catch (error) {
                    done(error);
                }
            });
        });

        it('Returns correct content on invalid ID.', function (done) {
            const result = request('http://localhost:7865/cart/hello', function (error, response, body) {
                if (error) {
                    return done(error);
                }

                try {
                    expect(body).to.equal('ID must be a number.');
                    done();
                } catch (error) {
                    done(error);
                }
            });
        });
    });

    describe('Payment Page', function () {
        it('Returns 200 status code.', function (done) {
            const result = request('http://localhost:7865/available_payments', function (error, response, body) {
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
            const result = request('http://localhost:7865/available_payments', function (error, response, body) {
                if (error) {
                    return done(error);
                }

                try {
                    expect(JSON.parse(body)).to.deep.equal({
                        payment_methods: {
                            credit_cards: true,
                            paypal: false
                        }
                    });
                    done();
                } catch (error) {
                    done(error);
                }
            });
        });
    });

    describe('Login Page', function () {
        it('Returns 200 status code on valid credentials.', function (done) {
            const result = request('http://localhost:7865/login', {
                method: 'POST',
                json: { userName: 'Test' }
            }, function (error, response, body) {
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

        it('Returns correct content on valid credentials.', function (done) {
            const result = request('http://localhost:7865/login', {
                method: 'POST',
                json: { userName: 'Test' }
            }, function (error, response, body) {
                if (error) {
                    return done(error);
                }

                try {
                    expect(body).to.equal("Welcome Test");
                    done();
                } catch (error) {
                    done(error);
                }
            });
        });
    });
});
