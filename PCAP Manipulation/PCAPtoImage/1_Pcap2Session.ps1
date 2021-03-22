foreach($f in files 1_Pcap *.pcap)
{
    0_Tool\SplitCap -p 50000 -b 50000 -r $f.FullName -o 2_Session\AllLayers\$($f.BaseName)-ALL
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2_Session\AllLayers\$($f.BaseName)-ALL
    files 2_Session\AllLayers\$($f.BaseName)-ALL | Where-Object{$_.Length -eq 0} | Remove-Item

    0_Tool\SplitCap -p 50000 -b 50000 -r $f.FullName -o 2_Session\L7\$($f.BaseName)-L7 -y L7
    # 0_Tool\SplitCap_2-1\SplitCap -p 50000 -b 50000 -r $f.FullName -s flow -o 2_Session\L7\$($f.BaseName)-L7 -y L7
    files 2_Session\L7\$($f.BaseName)-L7 | Where-Object{$_.Length -eq 0} | Remove-Item
}

0_Tool\finddupe -del 2_Session\AllLayers
0_Tool\finddupe -del 2_Session\L7