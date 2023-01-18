function buttonPress() {
  var bill = document.getElementById("billAmt").value;
  let n = 1;
  n = document.getElementById("peopleAmt").value;
  if (bill == "") {
    alert("Enter a Amount to divide");
  } else if(bill>0) {
    if(n=="")
    {
      n=1;
    }
    bill = bill / n;
    console.log("The bill is " + bill.toFixed(2));
    document.getElementById("demo").style.display = "block";
    document.getElementById("demo").innerHTML =
      "Contribution Per Person : " + bill;
  }
}
