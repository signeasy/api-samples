
class Originals
{
    name = "";
    id = 0;

    constructor(id, name)
  {
    this.id = id;
    this.name = name;
  }

  to_json(){
  return {"id": this.id, "name": this.name}
  }
}

module.exports = Originals