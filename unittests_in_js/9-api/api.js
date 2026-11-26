const express = require("express");

const app = express();
const PORT = 7865;

app.get("/", (req, res) => res.send("Welcome to the payment system"));

app.get("/cart/:id", (req, res) => {
    let id = req.params.id.trim();

    if (id !== '' && !Number.isNaN(Number(id))) {
        id = Number(id);
        res.send(`Payment methods for cart ${id}`);
    } else {
        res.status(404).send("ID must be a number.");
    }
})

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
