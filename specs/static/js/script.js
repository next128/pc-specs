'use strict';
var tab; // заголовок вкладки
var tabContent; // блок содержащий контент вкладки

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


window.onload = function() {
  tabContent = document.getElementsByClassName('tabContent');
  tab = document.getElementsByClassName('tab');
  hideTabsContent(1);
}

document.getElementById('tabs').onclick = function(event) {
  var target = event.target;
  if (target.className == 'tab') {
    for (var i = 0; i < tab.length; i++) {
      if (target == tab[i]) {
        showTabsContent(i);
        break;
      }
    }
  }
}

function hideTabsContent(a) {
  for (var i = a; i < tabContent.length; i++) {
    tabContent[i].classList.remove('show');
    tabContent[i].classList.add("hide");
    tab[i].classList.remove('whiteborder');
  }
}

function showTabsContent(b) {
  if (tabContent[b].classList.contains('hide')) {
    hideTabsContent(0);
    tab[b].classList.add('whiteborder');
    tabContent[b].classList.remove('hide');
    tabContent[b].classList.add('show');
  }
}