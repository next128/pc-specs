'use strict';

const { createApp } = Vue;

createApp({
  data() {
    return {
      currentTab: 'pc'
    };
  },
}).mount('#tabs');


tippy('#keyboard', {
  content: '<p style="font-size: 19px">BASE: Stock<br>SWITCHES: Durock T1<br>KEYCAPS: Stock<p>',
  followCursor: true,
  allowHTML: true
});


tippy('#case', {
  content: '<p style="font-size: 19px; width: 100%">TOP: Stock<br>BOTTOM: Dynamic X2 GP-18 PWM<br>FRONT: 3x Arctic P14 PWM<br>EXHAUST: Thermaltake Toughfan 12<p>',
  followCursor: true,
  allowHTML: true,
  maxWidth: '100%'
});