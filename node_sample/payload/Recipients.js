
class Recipients{
  role_id = 0;
  email = "";
  first_name = "";
  last_name = "";

    constructor(role_id, email, first_name, last_name="")
  {
    this.role_id = role_id;
    this.email = email;
    this.first_name = first_name;
    this.last_name = last_name;
  }

  to_json(){
  return  {"role_id": this.role_id, "email": this.email, "first_name": this.first_name, "last_name": this.last_name}
  }
}

module.exports = Recipients
