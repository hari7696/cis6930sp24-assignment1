03/09/2024 18:21:30 - root - INFO - PRE RUN unparsed Args parsing failed (Namespace(), ['--name', '--dates', '--phones', '--address', '--stats', 'stderr', '--output', 'gradescopetestsout/', '--input', 'text_files/testdatesin'])
03/09/2024 18:21:32 - root - INFO - starting main
03/09/2024 18:21:32 - root - INFO - spacy model loaded
03/09/2024 18:21:32 - root - INFO - creating output directory
03/09/2024 18:21:32 - root - INFO - text preprocessing done
03/09/2024 18:21:32 - root - INFO - entity extraction with spacy done
03/09/2024 18:21:32 - assignment1.regex_helper - INFO - regex matching started
03/09/2024 18:21:32 - assignment1.regex_helper - INFO - regex matching initial dictionary <class 'list'>
03/09/2024 18:21:32 - root - INFO - entity extraction with regex done
03/09/2024 18:21:32 - root - INFO - censoring done
03/09/2024 18:21:32 - root - INFO - for file text_files/testdatesin censoring dictionary: {'PERSON': [(268, 283, 'Phillip K Allen'), (290, 302, 'Tim Belden <'), (302, 312, 'Tim Belden'), (357, 370, 'Phillip Allen'), (381, 418, "Allen  Phillip K. 'Sent Mail\nX-Origin"), (420, 427, 'Allen-P'), (440, 446, 'pallen'), (36, 50, 'JavaMail.evans'), (108, 121, 'phillip.allen'), (136, 146, 'tim.belden'), (306, 318, 'Belden/Enron')], 'DATE': [(69, 80, '14 May 2001'), (81, 89, '16:39:00'), (69, 75, '14 May'), (181, 184, '1.0'), (371, 378, 'Jan2002')], 'PHONE': [(13, 35, '18782981.1075855378110'), (75, 83, ' 2001 16'), (87, 95, '00 -0700')], 'ADDRESS': [(157, 164, 'Subject')]}
03/09/2024 18:21:32 - root - INFO - preprocessed text Message-ID: <18782981.1075855378110.JavaMail.evans@thyme>
Date: Mon  14 May 2001 16:39:00 -0700 (PDT)
From: phillip.allen@enron.com
To: tim.belden@enron.com
Subject: 
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Phillip K Allen
X-To: Tim Belden <Tim Belden/Enron@EnronXGate>
X-cc: 
X-bcc: 
X-Folder:  Phillip Allen Jan2002 1 Allen  Phillip K. 'Sent Mail
X-Origin: Allen-P
X-FileName: pallen (Non-Privileged).pst

Here is our forecast

 
03/09/2024 18:21:32 - root - INFO - printing stats to stdout/ ouput directory
03/09/2024 18:21:32 - root - INFO - file written to a path gradescopetestsout/testdatesin.censored
03/09/2024 18:21:32 - root - INFO - written to output dir files in dir are ['testdatesin.censored']
03/09/2024 18:21:32 - root - INFO - censored file written to output directory
03/09/2024 18:21:32 - root - INFO - printing stats to stderr
03/09/2024 18:21:32 - root - INFO - main ended
03/09/2024 18:21:32 - root - INFO - censoring done
03/09/2024 18:21:32 - root - INFO - output dir ['testdatesin.censored']
03/09/2024 18:29:16 - root - INFO - PRE RUN unparsed Args parsing failed (Namespace(), ['--name', '--dates', '--phones', '--address', '--stats', 'stderr', '--output', 'gradescopetestsout/', '--input', 'text_files/testdatesin'])
03/09/2024 18:29:18 - root - INFO - starting main
03/09/2024 18:29:18 - root - INFO - spacy model loaded
03/09/2024 18:29:18 - root - INFO - text preprocessing done
03/09/2024 18:29:18 - root - INFO - entity extraction with spacy done
03/09/2024 18:29:18 - assignment1.regex_helper - INFO - regex matching started
03/09/2024 18:29:18 - assignment1.regex_helper - INFO - regex matching initial dictionary <class 'list'>
03/09/2024 18:29:18 - root - INFO - entity extraction with regex done
03/09/2024 18:29:18 - root - INFO - censoring done
03/09/2024 18:29:18 - root - INFO - for file text_files/testdatesin censoring dictionary: {'PERSON': [(268, 283, 'Phillip K Allen'), (290, 302, 'Tim Belden <'), (302, 312, 'Tim Belden'), (357, 370, 'Phillip Allen'), (381, 418, "Allen  Phillip K. 'Sent Mail\nX-Origin"), (420, 427, 'Allen-P'), (440, 446, 'pallen'), (36, 50, 'JavaMail.evans'), (108, 121, 'phillip.allen'), (136, 146, 'tim.belden'), (306, 318, 'Belden/Enron')], 'DATE': [(69, 80, '14 May 2001'), (81, 89, '16:39:00'), (69, 75, '14 May'), (181, 184, '1.0'), (371, 378, 'Jan2002')], 'PHONE': [(13, 35, '18782981.1075855378110'), (75, 83, ' 2001 16'), (87, 95, '00 -0700')], 'ADDRESS': [(157, 164, 'Subject')]}
03/09/2024 18:29:18 - root - INFO - preprocessed text Message-ID: <18782981.1075855378110.JavaMail.evans@thyme>
Date: Mon  14 May 2001 16:39:00 -0700 (PDT)
From: phillip.allen@enron.com
To: tim.belden@enron.com
Subject: 
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Phillip K Allen
X-To: Tim Belden <Tim Belden/Enron@EnronXGate>
X-cc: 
X-bcc: 
X-Folder:  Phillip Allen Jan2002 1 Allen  Phillip K. 'Sent Mail
X-Origin: Allen-P
X-FileName: pallen (Non-Privileged).pst

Here is our forecast

 
03/09/2024 18:29:18 - root - INFO - printing stats to stdout/ ouput directory
03/09/2024 18:29:18 - root - INFO - file written to a path gradescopetestsout/testdatesin.censored
03/09/2024 18:29:18 - root - INFO - written to output dir files in dir are ['testdatesin.censored']
03/09/2024 18:29:18 - root - INFO - censored file written to output directory
03/09/2024 18:29:18 - root - INFO - printing stats to stderr
03/09/2024 18:29:18 - root - INFO - main ended
03/09/2024 18:29:18 - root - INFO - censoring done
03/09/2024 18:29:18 - root - INFO - output dir ['testdatesin.censored']
03/09/2024 18:31:16 - root - INFO - PRE RUN unparsed Args parsing failed (Namespace(), ['--name', '--dates', '--phones', '--address', '--stats', 'stderr', '--output', 'gradescopetestsout/', '--input', 'text_files/testdatesin'])
03/09/2024 18:31:17 - root - INFO - starting main
03/09/2024 18:31:17 - root - INFO - spacy model loaded
03/09/2024 18:31:17 - root - INFO - text preprocessing done
03/09/2024 18:31:17 - root - INFO - entity extraction with spacy done
03/09/2024 18:31:17 - assignment1.regex_helper - INFO - regex matching started
03/09/2024 18:31:17 - assignment1.regex_helper - INFO - regex matching initial dictionary <class 'list'>
03/09/2024 18:31:17 - root - INFO - entity extraction with regex done
03/09/2024 18:31:17 - root - INFO - censoring done
03/09/2024 18:31:17 - root - INFO - for file text_files/testdatesin censoring dictionary: {'PERSON': [(268, 283, 'Phillip K Allen'), (290, 302, 'Tim Belden <'), (302, 312, 'Tim Belden'), (357, 370, 'Phillip Allen'), (381, 418, "Allen  Phillip K. 'Sent Mail\nX-Origin"), (420, 427, 'Allen-P'), (440, 446, 'pallen'), (36, 50, 'JavaMail.evans'), (108, 121, 'phillip.allen'), (136, 146, 'tim.belden'), (306, 318, 'Belden/Enron')], 'DATE': [(69, 80, '14 May 2001'), (81, 89, '16:39:00'), (69, 75, '14 May'), (181, 184, '1.0'), (371, 378, 'Jan2002')], 'PHONE': [(13, 35, '18782981.1075855378110'), (75, 83, ' 2001 16'), (87, 95, '00 -0700')], 'ADDRESS': [(157, 164, 'Subject')]}
03/09/2024 18:31:17 - root - INFO - preprocessed text Message-ID: <18782981.1075855378110.JavaMail.evans@thyme>
Date: Mon  14 May 2001 16:39:00 -0700 (PDT)
From: phillip.allen@enron.com
To: tim.belden@enron.com
Subject: 
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Phillip K Allen
X-To: Tim Belden <Tim Belden/Enron@EnronXGate>
X-cc: 
X-bcc: 
X-Folder:  Phillip Allen Jan2002 1 Allen  Phillip K. 'Sent Mail
X-Origin: Allen-P
X-FileName: pallen (Non-Privileged).pst

Here is our forecast

 
03/09/2024 18:31:17 - root - INFO - printing stats to stdout/ ouput directory
03/09/2024 18:31:17 - root - INFO - file written to a path gradescopetestsout/testdatesin.censored
03/09/2024 18:31:17 - root - INFO - written to output dir files in dir are ['testdatesin.censored']
03/09/2024 18:31:17 - root - INFO - censored file written to output directory
03/09/2024 18:31:17 - root - INFO - printing stats to stderr
03/09/2024 18:31:17 - root - INFO - main ended
03/09/2024 18:31:17 - root - INFO - censoring done
03/09/2024 18:31:17 - root - INFO - output dir ['testdatesin.censored']
