## PCAPs in 2_MAC grouped by sessions 

foreach($f in gci 2_MAC *.pcap)
{
    0_Tool\SplitCap -p 50000 -b 50000 -r $f.FullName -s session -o 2_Session\$($f.BaseName)
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2_Session\AllLayers\$($f.BaseName)-ALL
    gci 2_Session\$($f.BaseName)-ALL | Where-Object{$_.Length -eq 0} | Remove-Item
}

0_Tool\finddupe -del 2_Session