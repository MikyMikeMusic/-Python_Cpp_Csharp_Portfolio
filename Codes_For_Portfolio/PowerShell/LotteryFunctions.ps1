Function LotteryDraw{
    param ($min, $max, $quantity)
    for($i=0;$i -lt $quantity;$i++){
        Get-Random -Minimum $min -Maximum $max

    }
}

function LotteryDraw($min, $max, $quantity) 
{
    for ($i = 0; $i -lt $quantity; $i++) {
       Get-Random -Minimum $min -Maximum $max
    }
}

Write-Host "Testing Lottery Generator"
LotteryDraw 1 10 5  

function MatchThree() 
{
  Write-Host "Wlecome to the Match Three game"
  LotteryDraw 0 9 3 
}

MatchThree

function MegaLotto()
{
  Write-Host "Welcome to the Mega Lotto game"
  LotteryDraw 10000 99999 
}

MegaLotto

function MagicBall()
{
  Write-Host "Welcome to the Magic Ball game"
  LotteryDraw 10 99 6 
}

 MagicBall