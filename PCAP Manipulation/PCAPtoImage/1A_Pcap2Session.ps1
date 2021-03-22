## PCAPs in 1_Pcap grouped by mac address with -s option

foreach($f in gci 1_Pcap *.pcap)
{
    0_Tool\SplitCap -p 50000 -b 50000 -r $f.FullName -s mac -o 2_MAC\$($f.BaseName)-ALL
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2_Session\AllLayers\$($f.BaseName)-ALL
    gci 2_MAC\$($f.BaseName)-ALL | Where-Object{$_.Length -eq 0} | Remove-Item
}

0_Tool\finddupe -del 2_MAC