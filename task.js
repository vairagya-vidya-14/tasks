function displayAvg(){
    let n1=parseInt(document.getElementById("num1").value);
    let n2=parseInt(document.getElementById("num2").value);
    let n3=parseInt(document.getElementById("num3").value);
    let sum=n1+n2+n3;
    let avg=sum/3;
    document.getElementById("res1").value=avg

}

function displayAvgEx(){
    let n1=parseInt(document.getElementById("num4").value);
    let n2=parseInt(document.getElementById("num5").value);
    let n3=parseInt(document.getElementById("num6").value);
    let sum=n1+n2+n3;
    let avg=sum/3;
    document.getElementById("res2").value=avg

}

function sumNatural() {
    let n = parseInt(document.getElementById("sum").value);
    let result = n * (n + 1) / 2;
    document.getElementById("res3").value = result;
}

function avgNatural() {
    let n = parseInt(document.getElementById("avg").value);
    let sum = n * (n + 1) / 2;
    let avg=sum/n
    document.getElementById("res4").value = avg;
}

function displayProfit(){
    let cost_price=parseInt(document.getElementById("cost").value);
    let selling_price=parseInt(document.getElementById("selling").value);
    let profit=selling_price-cost_price
    let profit_per=(profit/cost_price)*100
    document.getElementById("res5").value=profit_per
    
    }

function simpleInterest(){
    let p=parseInt(document.getElementById("principal").value)
    let t=parseInt(document.getElementById("time").value)
    let r=parseInt(document.getElementById("rate").value)
    let simple_interest=(p*t*r)/100
    document.getElementById("res6").value=simple_interest
}

function missingAngle(){
    let angle1=parseInt(document.getElementById("angle1").value)
    let angle2=parseInt(document.getElementById("angle2").value)
    let sumAngles=angle1+angle2
    let missing_angle=180-sumAngles
    document.getElementById("res7").value=missing_angle
}

function lastDigit(){
    let n=parseInt(document.getElementById("last_digit").value)
    let ld=n%10
    document.getElementById("res8").value=ld
}

function remove_lastDigit(){
    let n=parseInt(document.getElementById("remove_digit").value)
    let ld=parseInt(n/10)
    document.getElementById("res9").value=ld
}

function first_digit(){

    let n = parseInt(document.getElementById("first_digit").value)

    let n1 = parseInt(n / 10)
    let fd = parseInt(n1 / 10)

    document.getElementById("res10").value = fd
}

function five_digit(){

    let n = parseInt(document.getElementById("five_digit").value)

    let n1 = parseInt(n / 10)
    let n2 = parseInt(n1 / 10)
    let n3 = parseInt(n2 / 10)
    let fd = parseInt(n3 / 10)
    

    document.getElementById("res11").value = fd
}

function celsius(){
    let c=parseInt(document.getElementById("celsius").value)
    let f=(c*9/5)+32
    document.getElementById("res12").value=f
}

function fahrenheit(){
    let f=parseInt(document.getElementById("fahrenheit").value)
    let c=(f-32)*5/9
    document.getElementById("res13").value=c
}

function grossSalary(){
    let basic_salary=parseInt(document.getElementById("salary").value)
    let hra=parseInt(document.getElementById("hra").value)
    let da=parseInt(document.getElementById("da").value)
    let gross_salary=basic_salary+hra+da
    document.getElementById("gross").value=gross_salary
}

function swapWithThird(){
    let a=parseInt(document.getElementById("swap1").value)
    let b=parseInt(document.getElementById("swap2").value)
    let c=a
    a=b
    b=c
    document.getElementById("res15").value="num1 = "+ a + ", num2 = "+b
}

function swapWithoutThird(){
    let a=parseInt(document.getElementById("swap3").value)
    let b=parseInt(document.getElementById("swap4").value)
    a=a+b
    b=a-b
    a=a-b
    document.getElementById("res16").value="num1 = "+ a + ", num2 = "+b
}