<h1>GitHub</h1>
<i>Post Commit Hook</i>
<?php
// The Public IP addresses for github hooks are: 207.97.227.253, 50.57.128.197, 108.171.174.178.
// if (ip2long($_SERVER['REMOTE_ADDR']) == -1 || ip2long($_SERVER['REMOTE_ADDR'] === FALSE)) {
// 	// Should never see this unless something screwy is up.
// 	die('Invalid IP from REMOTE_ADDR.');
// } else {
// 	switch ($_SERVER['REMOTE_ADDR']) {
// 		case gethostbyname('localhost'):
// 		case gethostbyname('home.vertigion.com'):
// 		case gethostbyname('CAS-D5QTPL1.unt.ad.unt.edu'):
// 		case gethostbyname('CAS-17DH1W1'):
// 		case gethostbyname('CAS-17DH1W1.unt.ad.unt.edu'):
// 		case gethostbyname('CAS-H6DDYH1'):
// 		case gethostbyname('CAS-H6DDYH1.unt.ad.unt.edu'):
// 		case '207.97.227.253':
// 		case '50.57.128.197':
// 		case '108.171.174.178':
// 			echo "Authorized IP address detected, continuing ...\n";
// 			break;
// 		default:
// 			die('Not Authorized!');
// 	}
// }
?>
<pre>
<?php
$kill = array();
$execk = exec('killall -9 /home/lurkin4life/.virtualenv/csce4350/bin/python', $kill);
print_r($kill);
?>
</pre><pre>
<?php
$out = array();
$exec = exec('cd /var/www/vertigion; git reset --hard HEAD; git pull', $out);
print_r($out);
?>
</pre><pre>
<?php
`/home/lurkin4life/.virtualenv/csce4350/bin/python /home/lurkin4life/com.worleybox.csce4350/manage.py runserver 0.0.0.0:4498 > /dev/null 2>/dev/null &`;

if ($out[0] == 'Already up-to-date.') {
	`touch /tmp/AR_FILE_GITHUB_V3PU_HOOK`;
	echo 'AR file created.';
}
?>