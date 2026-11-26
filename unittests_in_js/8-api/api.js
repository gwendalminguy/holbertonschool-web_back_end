const express = require("express");

const app = express();
const PORT = 7865;

app.get("/", (req, res) => res.send("Welcome to the payment system"));

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
