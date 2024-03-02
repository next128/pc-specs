'use strict';

const { createApp, ref } = Vue;
const { createVuetify } = Vuetify;

const vuetify = createVuetify({
    icons: {
        defaultSet: 'mdi', // This is already the default value - only for display purposes
    },
})


createApp ({
  data() {
    return {
      currentTab: 'pc',
    };
  },
}).use(vuetify).mount('body');


let paragraphs = document.getElementsByTagName("p");
for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].innerHTML = (paragraphs[i].textContent).replaceAll("repl", "<br>");
}

let inp = document.querySelectorAll("input");
let btn = document.getElementById('save');

for (let i = 0; i < inp.length; i++) {
    inp[i].addEventListener('input', function (e) {
        btn.disabled = '';
    });
}

