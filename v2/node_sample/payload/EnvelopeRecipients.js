const Recipients = require('./Recipients');

class EnvelopeRecipients extends Recipients{
    constructor(role_id, email, first_name, last_name="")
  {
    super(role_id, email, first_name, last_name="")
  }

  to_json(){
  var obj = super.to_json()
  obj['recipient_id'] = obj['role_id'];
  delete obj['role_id'];
  return  obj
  }
}

module.exports = EnvelopeRecipients