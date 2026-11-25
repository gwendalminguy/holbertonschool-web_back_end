function calculateNumber(type, a, b) {
    a = Math.round(a);
    b = Math.round(b);

    switch (type) {
        case 'SUM':
            return a + b;
        case 'SUBSTRACT':
            return a - b;
        case 'DIVIDE':
            if (b === 0) {
                return 'Error';
            } else {
                return a / b;
            }
    }
}

module.exports = calculateNumber;
