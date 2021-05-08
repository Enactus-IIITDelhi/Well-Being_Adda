const helptexts = document.querySelectorAll('.helptext');
for(let i=0; i<helptexts.length; i++) {
    let ih = helptexts[i].innerHTML;
    ih = "<br>" + ih;
    helptexts[i].innerHTML = ih;
}