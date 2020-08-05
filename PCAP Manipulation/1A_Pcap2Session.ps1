##Split PCAP files by MAC address (per device) using powershell script
foreach($f in gci 1_Pcap *.pcap)
{
    splitcap -p 50000 -b 50000 -s mac -r $f.FullName -o 2A_MAC\AllLayers\$($f.BaseName)-ALL
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2A_MAC\AllLayers\$($f.BaseName)-ALL
    gci 2A_MAC\AllLayers\$($f.BaseName)-ALL | ?{$_.Length -eq 0} | del
}

0_Tool\finddupe -del 2A_MAC\AllLayers
