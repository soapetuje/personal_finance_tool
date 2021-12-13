document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#id_currency').addEventListener('click', () => update_currency());
    document.querySelector('#id_education').addEventListener('change', () => filter_education());
    document.querySelector('#id_race').addEventListener('change', () => filter_race());
    document.querySelector('#id_ethnicity').addEventListener('change', () => filter_ethnicity());
    document.querySelector('#id_age_group').addEventListener('change', () => filter_age());

    // Change hover background color if value is negative
    document.querySelectorAll('.card-title').forEach(number => {
      if (parseFloat(number.innerHTML) < 0) {
        var card = number.parentElement.parentElement;
        card.classList.add('card_danger');
      };
    });
  });


function update_currency() {
  const current_currency = document.querySelector('#id_currency').value;
  // console.log('focusing')
  document.querySelector('#id_currency').onchange = function (event) {
    // fields to send
    const current_finance = {
    income: document.querySelector('#income').innerHTML,
    assets: document.querySelector('#assets').innerHTML,
    debts: document.querySelector('#liabilities').innerHTML,
    net_worth: document.querySelector('#net_worth').innerHTML,
    old_currency: current_currency,
    new_currency: document.querySelector('#id_currency').value
    };
    // console.log(current_finance)
    // send request
    fetch('/update', {
    method: "POST",
    body: JSON.stringify(current_finance)
    })
    .then(response => response.json())
    .then(result => {

    // console.log(Object.values(result))
    // update HTML
    document.querySelector('#income').innerHTML = Object.values(result)[0];
    document.querySelector('#assets').innerHTML = Object.values(result)[1];
    document.querySelector('#liabilities').innerHTML = Object.values(result)[2];
    document.querySelector('#net_worth').innerHTML = Object.values(result)[3];
    document.querySelector('.display_currency').innerHTML = document.querySelector('#id_currency').value;
    document.querySelectorAll('.display_currency').forEach(display_currency => {
      display_currency.innerHTML = document.querySelector('#id_currency').value;
    });
    })
    .catch((error) => {
    console.error('Error:', error);
    });
  };
};
    
function filter_education() {
  const selection = {
  education: document.querySelector('#id_education').value
  };
  document.querySelector('#id_race').value = 'AL';
  document.querySelector('#id_ethnicity').value = 'AL';
  document.querySelector('#id_age_group').value = 0;

  fetch('/filter_education', {
  method: "POST",
  body: JSON.stringify(selection)
  })
  .then(response => response.json())
  .then(result => {
  // console.log(Object.values(result))
  document.querySelector('#income_p').innerHTML = Object.values(result)[0];
  document.querySelector('#assets_p').innerHTML = Object.values(result)[1];
  document.querySelector('#liabilities_p').innerHTML = Object.values(result)[2];
  document.querySelector('#net_worth_p').innerHTML = Object.values(result)[3];
  document.querySelector('#income_s').innerHTML = Object.values(result)[5];
  document.querySelector('#assets_s').innerHTML = Object.values(result)[6];
  document.querySelector('#liabilities_s').innerHTML = Object.values(result)[7];
  document.querySelector('#net_worth_s').innerHTML = Object.values(result)[8];
  document.querySelector('#user_count').innerHTML = Object.values(result)[9];

  document.querySelectorAll('.message').forEach(filter_message => {
    if (Object.values(result)[4]) {
      filter_message.style.display = "none";
    } else {
      filter_message.style.display = "inline";
    };
  });
  })
  .catch((error) => {
  console.error('Error:', error);
  });
};

 
function filter_race() {
  const selection = {
  race: document.querySelector('#id_race').value,
  };
  document.querySelector('#id_education').value = 'AL';
  document.querySelector('#id_ethnicity').value = 'AL';
  document.querySelector('#id_age_group').value = 0;

  fetch('/filter_race', {
  method: "POST",
  body: JSON.stringify(selection)
  })
  .then(response => response.json())
  .then(result => {
  // console.log(Object.values(result))
  document.querySelector('#income_p').innerHTML = Object.values(result)[0];
  document.querySelector('#assets_p').innerHTML = Object.values(result)[1];
  document.querySelector('#liabilities_p').innerHTML = Object.values(result)[2];
  document.querySelector('#net_worth_p').innerHTML = Object.values(result)[3];
  document.querySelector('#income_s').innerHTML = Object.values(result)[5];
  document.querySelector('#assets_s').innerHTML = Object.values(result)[6];
  document.querySelector('#liabilities_s').innerHTML = Object.values(result)[7];
  document.querySelector('#net_worth_s').innerHTML = Object.values(result)[8];
  document.querySelector('#user_count').innerHTML = Object.values(result)[9];

  document.querySelectorAll('.message').forEach(filter_message => {
    if (Object.values(result)[4]) {
      filter_message.style.display = "none";
    } else {
      filter_message.style.display = "inline";
    };
  });
  })
  .catch((error) => {
  console.error('Error:', error);
  });
};  

function filter_ethnicity() {
  const selection = {
  ethnicity: document.querySelector('#id_ethnicity').value,
  };
  document.querySelector('#id_education').value = 'AL';
  document.querySelector('#id_race').value = 'AL';
  document.querySelector('#id_age_group').value = 0;

  fetch('/filter_ethnicity', {
  method: "POST",
  body: JSON.stringify(selection)
  })
  .then(response => response.json())
  .then(result => {
  // console.log(Object.values(result))
  document.querySelector('#income_p').innerHTML = Object.values(result)[0];
  document.querySelector('#assets_p').innerHTML = Object.values(result)[1];
  document.querySelector('#liabilities_p').innerHTML = Object.values(result)[2];
  document.querySelector('#net_worth_p').innerHTML = Object.values(result)[3];
  document.querySelector('#income_s').innerHTML = Object.values(result)[5];
  document.querySelector('#assets_s').innerHTML = Object.values(result)[6];
  document.querySelector('#liabilities_s').innerHTML = Object.values(result)[7];
  document.querySelector('#net_worth_s').innerHTML = Object.values(result)[8];
  document.querySelector('#user_count').innerHTML = Object.values(result)[9];
  

  document.querySelectorAll('.message').forEach(filter_message => {
    if (Object.values(result)[4]) {
      filter_message.style.display = "none";
    } else {
      filter_message.style.display = "inline";
    };
  });
  })
  .catch((error) => {
  console.error('Error:', error);
  });
};  

function filter_age() {
  const selection = {
  age_group: document.querySelector('#id_age_group').value,
  };
  document.querySelector('#id_education').value = 'AL';
  document.querySelector('#id_race').value = 'AL';
  document.querySelector('#id_ethnicity').value = 'AL';

  fetch('/filter_age', {
  method: "POST",
  body: JSON.stringify(selection)
  })
  .then(response => response.json())
  .then(result => {
  // console.log(Object.values(result))
  document.querySelector('#income_p').innerHTML = Object.values(result)[0];
  document.querySelector('#assets_p').innerHTML = Object.values(result)[1];
  document.querySelector('#liabilities_p').innerHTML = Object.values(result)[2];
  document.querySelector('#net_worth_p').innerHTML = Object.values(result)[3];
  document.querySelector('#income_s').innerHTML = Object.values(result)[5];
  document.querySelector('#assets_s').innerHTML = Object.values(result)[6];
  document.querySelector('#liabilities_s').innerHTML = Object.values(result)[7];
  document.querySelector('#net_worth_s').innerHTML = Object.values(result)[8];
  document.querySelector('#user_count').innerHTML = Object.values(result)[9];

  document.querySelectorAll('.message').forEach(filter_message => {
    if (Object.values(result)[4]) {
      filter_message.style.display = "none";
    } else {
      filter_message.style.display = "inline";
    };
  });
  })
  .catch((error) => {
  console.error('Error:', error);
  });
};  