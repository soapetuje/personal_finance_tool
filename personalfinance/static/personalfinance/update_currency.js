document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#id_currency').addEventListener('click', () => update_currency());
  });


function update_currency() {
  const current_currency = document.querySelector('#id_currency').value;
  // console.log('focusing')
  document.querySelector('#id_currency').onchange = function (event) {
    // get fields to send
    const current_finance = {
    income: document.querySelector('#id_income').value,
    assets: document.querySelector('#id_assets').value,
    debts: document.querySelector('#id_debts').value,
    old_currency: current_currency,
    new_currency: document.querySelector('#id_currency').value
    };
    // console.log(current_finance)
    // make request
    fetch('/update', {
    method: "POST",
    body: JSON.stringify(current_finance)
    })
    .then(response => response.json())
    .then(result => {

    // console.log(Object.values(result))
    //update HTML
    document.querySelector('#id_income').value = Object.values(result)[0];
    document.querySelector('#id_assets').value = Object.values(result)[1];
    document.querySelector('#id_debts').value = Object.values(result)[2];
    })
    .catch((error) => {
    console.error('Error:', error);
    });
  };
};
  