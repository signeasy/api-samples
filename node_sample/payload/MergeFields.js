
class MergeFields{
    label = ""
    value = ""
    font = 0

    constructor(label, value, font=0)
  {
    this.label = label;
    this.value = value;
    this.font = font
  }

  to_json(){
  return {"label": this.label, "value": this.value, "font": this.font}
  }
}

module.exports = MergeFields