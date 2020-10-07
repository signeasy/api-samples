
class CC
{
    email = "";

    constructor(email)
  {
    this.email = email;
  }

  to_json(){
  return {"email": this.email}
  }
}

module.exports = CC