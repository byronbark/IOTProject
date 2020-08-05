foreach($f in gci .\2A_MAC\AllLayers *.pcap)
{
    splitcap -p 10000 -b 10000 -r $f.FullName -o 2B_Session\AllLayers\$($f.BaseName)-ALL
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2A_MAC\AllLayers\$($f.BaseName)-ALL
    gci 2B_Session\AllLayers\$($f.BaseName)-ALL | ?{$_.Length -eq 0} | del

    splitcap -p 10000 -b 10000 -r $f.FullName -o 2B_Session\L7\$($f.BaseName)-L7 -y L7
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2A_MAC\AllLayers\$($f.BaseName)-ALL
    gci 2B_Session\L7\$($f.BaseName)-L7 | ?{$_.Length -eq 0} | del
}

0_Tool\finddupe -del 2B_Session\AllLayers
0_Tool\finddupe -del 2B_Session\L7
