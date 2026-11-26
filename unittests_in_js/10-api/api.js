const express = require("express");

const app = express();
const PORT = 7865;

app.use(express.json());

// Home
app.get("/", (req, res) => res.send("Welcome to the payment system"));

// Cart
app.get("/cart/:id", (req, res) => {
    let id = req.params.id.trim();

    if (id !== '' && !Number.isNaN(Number(id))) {
        id = Number(id);
        res.send(`Payment methods for cart ${id}`);
    } else {
        res.status(404).send("ID must be a number.");
    }
})

// Payment
app.get("/available_payments", (req, res) => {
    res.send({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
})

// Login
app.post("/login", (req, res) => {
    const data = req.body;

    res.send(`Welcome ${data.userName}`);
})

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
