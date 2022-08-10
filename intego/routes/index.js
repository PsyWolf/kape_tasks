const express = require("express");
var validator = require("email-validator");
const bcrypt = require("bcrypt");
var db = require("../database");
const router = express.Router();

/* GET home page. */
router.get("/", function (req, res, next) {
  res.render("index", {
    title: "Register - Intego",
    success: false,
    emailError: false,
    name: "",
    email: "",
    company: "",
    pswd: "",
  });
});

router.post("/register", function (req, res, next) {
  var email = req.body.email;
  var name = req.body.name;
  var company = req.body.company;
  var password = req.body.password;

  if (!validator.validate(email)) {
    res.render("index", {
      title: "Register - Intego",
      success: false,
      emailError: "Invalid email address, please try again",
      name: name,
      email: email,
      company: company,
      pswd: password,
    });
    return;
  }

  bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(password, salt, function (err, hash) {
      if (err) throw err;
      var sql = `INSERT INTO users (email, name, company, pswd) VALUES ("${email}", "${name}", "${company}", "${hash}")`;
      db.query(sql, function (err, result) {
        if (err) throw err;
        console.log("record inserted");
        res.render("index", {
          title: "Register - Intego",
          success: true,
          emailError: false,
          name: "",
          email: "",
          company: "",
          pswd: "",
        });
      });
    });
  });
});

module.exports = router;
