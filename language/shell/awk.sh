echo -e "1\n2\n3\n4\n5\n6\ndsp\ndsa" | awk '
BEGIN {
    click_mode_set[1] = 1;
    click_mode_set[4] = 1;
    click_mode_set[5] = 1;
    click_mode_set[6] = 1;
    click_mode_set["dsp"] = 1;
}
{
    if (click_mode_set[$0]) {
        print $0;
    }
}
'
