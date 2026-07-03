"""Lightweight i18n for English, Hindi, and Kannada."""
from flask import session

SUPPORTED = ['en', 'hi', 'kn']

LANG_LABELS = {
    'en': 'English',
    'hi': 'हिन्दी',
    'kn': 'ಕನ್ನಡ',
}

# fmt: off
TRANSLATIONS = {
    # ── Nav & layout ──
    'browse_items':       {'en': 'Browse Items',       'hi': 'वस्तुएं देखें',           'kn': 'ವಸ್ತುಗಳನ್ನು ನೋಡಿ'},
    'browse_needs':       {'en': 'Browse Needs',       'hi': 'जरूरतें देखें',           'kn': 'ಅಗತ್ಯಗಳನ್ನು ನೋಡಿ'},
    'dashboard':          {'en': 'Dashboard',          'hi': 'डैशबोर्ड',                'kn': 'ಡ್ಯಾಶ್‌ಬೋರ್ಡ್'},
    'admin':              {'en': 'Admin',              'hi': 'व्यवस्थापक',              'kn': 'ನಿರ್ವಾಹಕ'},
    'login':              {'en': 'Login',              'hi': 'लॉग इन',                  'kn': 'ಲಾಗಿನ್'},
    'register':           {'en': 'Register',           'hi': 'पंजीकरण',                 'kn': 'ನೋಂದಣಿ'},
    'logout':             {'en': 'Logout',             'hi': 'लॉग आउट',                 'kn': 'ಲಾಗ್ ಔಟ್'},
    'footer_tagline':     {'en': 'Bridging generosity and need.',
                           'hi': 'उदारता और जरूरत को जोड़ना।',
                           'kn': 'ಉದಾರತೆ ಮತ್ತು ಅಗತ್ಯವನ್ನು ಸೇತುವೆ ಮಾಡುವುದು.'},

    # ── Home page ──
    'home_title':         {'en': 'AaryaSetu — Bridge of Giving', 'hi': 'आर्यसेतु — दान का पुल', 'kn': 'ಆರ್ಯಸೇತು — ದಾನದ ಸೇತುವೆ'},
    'hero_pill':          {'en': 'Bridging Generosity & Need', 'hi': 'उदारता और जरूरत को जोड़ना', 'kn': 'ಉದಾರತೆ ಮತ್ತು ಅಗತ್ಯವನ್ನು ಸೇತುವೆ ಮಾಡುವುದು'},
    'hero_give':          {'en': 'Give',               'hi': 'दें',                     'kn': 'ಕೊಡಿ'},
    'hero_more':          {'en': 'More.',              'hi': 'अधिक।',                   'kn': 'ಹೆಚ್ಚು.'},
    'hero_need':          {'en': 'Need',               'hi': 'जरूरत',                   'kn': 'ಅಗತ್ಯ'},
    'hero_less':          {'en': 'Less.',              'hi': 'कम।',                     'kn': 'ಕಡಿಮೆ.'},
    'hero_subtitle':      {'en': 'AaryaSetu connects donors, institutions & volunteers — turning surplus into smiles across communities.',
                           'hi': 'आर्यसेतु दानकर्ताओं, संस्थानों और स्वयंसेवकों को जोड़ता है — अतिरिक्त को समुदायों में मुस्कान में बदलता है।',
                           'kn': 'ಆರ್ಯಸೇತು ದಾನಿಗಳು, ಸಂಸ್ಥೆಗಳು ಮತ್ತು ಸ್ವಯಂಸೇವಕರನ್ನು ಸಂಪರ್ಕಿಸುತ್ತದೆ — ಅತಿರಿಕ್ತವನ್ನು ಸಮುದಾಯಗಳಲ್ಲಿ ನಗುಗಳಾಗಿ ಪರಿವರ್ತಿಸುತ್ತದೆ.'},
    'post_a_need':        {'en': 'Post a Need',        'hi': 'जरूरत पोस्ट करें',        'kn': 'ಅಗತ್ಯವನ್ನು ಪೋಸ್ಟ್ ಮಾಡಿ'},
    'donate_item':        {'en': 'Donate an Item',     'hi': 'वस्तु दान करें',          'kn': 'ವಸ್ತು ದಾನ ಮಾಡಿ'},
    'donors':             {'en': 'Donors',             'hi': 'दानकर्ता',                'kn': 'ದಾನಿಗಳು'},
    'institutions':       {'en': 'Institutions',       'hi': 'संस्थाएं',                'kn': 'ಸಂಸ್ಥೆಗಳು'},
    'volunteers':         {'en': 'Volunteers',         'hi': 'स्वयंसेवक',               'kn': 'ಸ್ವಯಂಸೇವಕರು'},
    'simple_process':     {'en': 'Simple Process',     'hi': 'सरल प्रक्रिया',           'kn': 'ಸರಳ ಪ್ರಕ್ರಿಯೆ'},
    'how_it_works':       {'en': 'How AaryaSetu Works','hi': 'आर्यसेतु कैसे काम करता है', 'kn': 'ಆರ್ಯಸೇತು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ'},
    'step1_title':        {'en': 'Register & Choose Role', 'hi': 'पंजीकरण करें और भूमिका चुनें', 'kn': 'ನೋಂದಣಿ ಮಾಡಿ ಮತ್ತು ಪಾತ್ರ ಆಯ್ಕೆಮಾಡಿ'},
    'step1_desc':         {'en': 'Sign up as a Donor, Institution, or Volunteer. Each role unlocks a personalised dashboard built for your needs.',
                           'hi': 'दानकर्ता, संस्थान या स्वयंसेवक के रूप में साइन अप करें। प्रत्येक भूमिका आपकी जरूरतों के लिए व्यक्तिगत डैशबोर्ड खोलती है।',
                           'kn': 'ದಾನಿ, ಸಂಸ್ಥೆ ಅಥವಾ ಸ್ವಯಂಸೇವಕರಾಗಿ ಸೈನ್ ಅಪ್ ಮಾಡಿ. ಪ್ರತಿ ಪಾತ್ರವು ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗಾಗಿ ವೈಯಕ್ತಿಕ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ತೆರೆಯುತ್ತದೆ.'},
    'step2_title':        {'en': 'Post or Browse',     'hi': 'पोस्ट करें या ब्राउज़ करें', 'kn': 'ಪೋಸ್ಟ್ ಮಾಡಿ ಅಥವಾ ಬ್ರೌಸ್ ಮಾಡಿ'},
    'step2_desc':         {'en': 'Donors list available items. Institutions post what they need. Both can browse each other\'s listings instantly.',
                           'hi': 'दानकर्ता उपलब्ध वस्तुएं सूचीबद्ध करते हैं। संस्थाएं अपनी जरूरतें पोस्ट करती हैं। दोनों एक-दूसरे की सूचियां तुरंत देख सकते हैं।',
                           'kn': 'ದಾನಿಗಳು ಲಭ್ಯವಿರುವ ವಸ್ತುಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತಾರೆ. ಸಂಸ್ಥೆಗಳು ತಮ್ಮ ಅಗತ್ಯಗಳನ್ನು ಪೋಸ್ಟ್ ಮಾಡುತ್ತವೆ. ಇಬ್ಬರೂ ಪರಸ್ಪರ ಪಟ್ಟಿಗಳನ್ನು ತಕ್ಷಣ ಬ್ರೌಸ್ ಮಾಡಬಹುದು.'},
    'step3_title':        {'en': 'Connect & Deliver',  'hi': 'जुड़ें और वितरित करें',   'kn': 'ಸಂಪರ್ಕಿಸಿ ಮತ್ತು ತಲುಪಿಸಿ'},
    'step3_desc':         {'en': 'Accept a match, coordinate pickup or delivery with volunteer help, and complete the donation — making a real difference.',
                           'hi': 'मिलान स्वीकार करें, स्वयंसेवक की मदद से पिकअप या डिलीवरी का समन्वय करें, और दान पूरा करें — वास्तविक बदलाव लाएं।',
                           'kn': 'ಹೊಂದಾಣಿಕೆಯನ್ನು ಸ್ವೀಕರಿಸಿ, ಸ್ವಯಂಸೇವಕರ ಸಹಾಯದಿಂದ ಪಿಕಪ್ ಅಥವಾ ವಿತರಣೆಯನ್ನು ಸಂಯೋಜಿಸಿ, ಮತ್ತು ದಾನವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ — ನಿಜವಾದ ಬದಲಾವಣೆ ಮಾಡಿ.'},
    'community':          {'en': 'Community',          'hi': 'समुदाय',                  'kn': 'ಸಮುದಾಯ'},
    'built_for_all':      {'en': 'Built for Everyone', 'hi': 'सभी के लिए बनाया गया',    'kn': 'ಎಲ್ಲರಿಗಾಗಿ ನಿರ್ಮಿಸಲಾಗಿದೆ'},
    'donors_desc':        {'en': 'Have clothes, food, stationery or appliances to give? Post items and let institutions that need them find you directly.',
                           'hi': 'कपड़े, भोजन, स्टेशनरी या उपकरण देने हैं? वस्तुएं पोस्ट करें और जरूरतमंद संस्थाएं आपको सीधे खोज सकें।',
                           'kn': 'ಬಟ್ಟೆ, ಆಹಾರ, ಸ್ಟೇಷನರಿ ಅಥವಾ ಉಪಕರಣಗಳನ್ನು ಕೊಡಲು ಇದೆಯೇ? ವಸ್ತುಗಳನ್ನು ಪೋಸ್ಟ್ ಮಾಡಿ ಮತ್ತು ಅಗತ್ಯವಿರುವ ಸಂಸ್ಥೆಗಳು ನಿಮ್ಮನ್ನು ನೇರವಾಗಿ ಹುಡುಕಲಿ.'},
    'institutions_desc':  {'en': 'Old age homes, orphanages, shelters — post your needs and browse available donations, all in one place.',
                           'hi': 'वृद्धाश्रम, अनाथालय, आश्रय — अपनी जरूरतें पोस्ट करें और उपलब्ध दान ब्राउज़ करें, सब एक जगह।',
                           'kn': 'ವೃದ್ಧಾಶ್ರಮಗಳು, ಅನಾಥಾಲಯಗಳು, ಆಶ್ರಯಗಳು — ನಿಮ್ಮ ಅಗತ್ಯಗಳನ್ನು ಪೋಸ್ಟ್ ಮಾಡಿ ಮತ್ತು ಲಭ್ಯವಿರುವ ದಾನಗಳನ್ನು ಬ್ರೌಸ್ ಮಾಡಿ, ಎಲ್ಲಾ ಒಂದೇ ಸ್ಥಳದಲ್ಲಿ.'},
    'volunteers_desc':    {'en': 'Help coordinate, pick up and deliver donations between donors and institutions. Be the bridge that makes it happen.',
                           'hi': 'दानकर्ताओं और संस्थानों के बीच दान का समन्वय, पिकअप और वितरण में मदद करें। वह पुल बनें जो इसे संभव बनाता है।',
                           'kn': 'ದಾನಿಗಳು ಮತ್ತು ಸಂಸ್ಥೆಗಳ ನಡುವೆ ದಾನಗಳ ಸಂಯೋಜನೆ, ಪಿಕಪ್ ಮತ್ತು ವಿತರಣೆಯಲ್ಲಿ ಸಹಾಯ ಮಾಡಿ. ಅದನ್ನು ಸಾಧ್ಯವಾಗಿಸುವ ಸೇತುವೆಯಾಗಿ.'},
    'join_donor':         {'en': 'Join as Donor →',    'hi': 'दानकर्ता के रूप में जुड़ें →', 'kn': 'ದಾನಿಯಾಗಿ ಸೇರಿ →'},
    'join_institution':   {'en': 'Join as Institution →', 'hi': 'संस्था के रूप में जुड़ें →', 'kn': 'ಸಂಸ್ಥೆಯಾಗಿ ಸೇರಿ →'},
    'join_volunteer':     {'en': 'Join as Volunteer →','hi': 'स्वयंसेवक के रूप में जुड़ें →', 'kn': 'ಸ್ವಯಂಸೇವಕರಾಗಿ ಸೇರಿ →'},
    'ready_cta':          {'en': 'Ready to Make a Difference?', 'hi': 'बदलाव लाने के लिए तैयार हैं?', 'kn': 'ಬದಲಾವಣೆ ಮಾಡಲು ಸಿದ್ಧರಿದ್ದೀರಾ?'},
    'join_cta_desc':      {'en': 'Join AaryaSetu today and become part of a community that cares.',
                           'hi': 'आज ही आर्यसेतु से जुड़ें और एक देखभाल करने वाले समुदाय का हिस्सा बनें।',
                           'kn': 'ಇಂದೇ ಆರ್ಯಸೇತುವಿಗೆ ಸೇರಿ ಮತ್ತು ಕಾಳಜಿ ವಹಿಸುವ ಸಮುದಾಯದ ಭಾಗವಾಗಿ.'},
    'get_started':        {'en': "Get Started — It's Free", 'hi': 'शुरू करें — यह मुफ़्त है', 'kn': 'ಪ್ರಾರಂಭಿಸಿ — ಇದು ಉಚಿತ'},

    # ── Login / Register ──
    'email':              {'en': 'Email',              'hi': 'ईमेल',                    'kn': 'ಇಮೇಲ್'},
    'password':           {'en': 'Password',           'hi': 'पासवर्ड',                 'kn': 'ಪಾಸ್‌ವರ್ಡ್'},
    'join_aaryasetu':     {'en': 'Join AaryaSetu',     'hi': 'आर्यसेतु से जुड़ें',      'kn': 'ಆರ್ಯಸೇತುವಿಗೆ ಸೇರಿ'},
    'create_account_desc':{'en': 'Create your account to start making a difference',
                           'hi': 'बदलाव लाने के लिए अपना खाता बनाएं',
                           'kn': 'ಬದಲಾವಣೆ ಮಾಡಲು ನಿಮ್ಮ ಖಾತೆಯನ್ನು ರಚಿಸಿ'},
    'full_name':          {'en': 'Full Name',          'hi': 'पूरा नाम',                'kn': 'ಪೂರ್ಣ ಹೆಸರು'},
    'enter_full_name':    {'en': 'Enter your full name','hi': 'अपना पूरा नाम दर्ज करें', 'kn': 'ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರನ್ನು ನಮೂದಿಸಿ'},
    'email_address':      {'en': 'Email Address',      'hi': 'ईमेल पता',                'kn': 'ಇಮೇಲ್ ವಿಳಾಸ'},
    'enter_email':        {'en': 'Enter your email',   'hi': 'अपना ईमेल दर्ज करें',     'kn': 'ನಿಮ್ಮ ಇಮೇಲ್ ನಮೂದಿಸಿ'},
    'phone_number':       {'en': 'Phone Number',       'hi': 'फ़ोन नंबर',               'kn': 'ಫೋನ್ ಸಂಖ್ಯೆ'},
    'optional':           {'en': '(optional)',         'hi': '(वैकल्पिक)',              'kn': '(ಐಚ್ಛಿಕ)'},
    'address':            {'en': 'Address',            'hi': 'पता',                     'kn': 'ವಿಳಾಸ'},
    'address_hint':       {'en': '(recommended for institutions)', 'hi': '(संस्थाओं के लिए अनुशंसित)', 'kn': '(ಸಂಸ್ಥೆಗಳಿಗೆ ಶಿಫಾರಸು)'},
    'confirm_password':   {'en': 'Confirm Password',   'hi': 'पासवर्ड की पुष्टि करें',  'kn': 'ಪಾಸ್‌ವರ್ಡ್ ದೃಢೀಕರಿಸಿ'},
    'join_as':            {'en': 'I want to join as',  'hi': 'मैं इस रूप में जुड़ना चाहता/चाहती हूं', 'kn': 'ನಾನು ಇದಾಗಿ ಸೇರಲು ಬಯಸುತ್ತೇನೆ'},
    'role_donor':         {'en': 'Donor',              'hi': 'दानकर्ता',                'kn': 'ದಾನಿ'},
    'role_donor_desc':    {'en': 'I want to donate items to those in need', 'hi': 'मैं जरूरतमंदों को वस्तुएं दान करना चाहता/चाहती हूं', 'kn': 'ನಾನು ಅಗತ್ಯವಿರುವವರಿಗೆ ವಸ್ತುಗಳನ್ನು ದಾನ ಮಾಡಲು ಬಯಸುತ್ತೇನೆ'},
    'role_institution':   {'en': 'Institution',        'hi': 'संस्था',                  'kn': 'ಸಂಸ್ಥೆ'},
    'role_institution_desc': {'en': 'I represent an orphanage or old age home', 'hi': 'मैं एक अनाथालय या वृद्धाश्रम का प्रतिनिधित्व करता/करती हूं', 'kn': 'ನಾನು ಅನಾಥಾಲಯ ಅಥವಾ ವೃದ್ಧಾಶ್ರಮವನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತೇನೆ'},
    'role_volunteer':     {'en': 'Volunteer',          'hi': 'स्वयंसेवक',               'kn': 'ಸ್ವಯಂಸೇವಕ'},
    'role_volunteer_desc':{'en': 'I want to help coordinate and deliver donations', 'hi': 'मैं दान का समन्वय और वितरण में मदद करना चाहता/चाहती हूं', 'kn': 'ನಾನು ದಾನಗಳ ಸಂಯೋಜನೆ ಮತ್ತು ವಿತರಣೆಯಲ್ಲಿ ಸಹಾಯ ಮಾಡಲು ಬಯಸುತ್ತೇನೆ'},
    'create_account':     {'en': 'Create Account',     'hi': 'खाता बनाएं',              'kn': 'ಖಾತೆ ರಚಿಸಿ'},
    'already_have':       {'en': 'Already have an account?', 'hi': 'पहले से खाता है?', 'kn': 'ಈಗಾಗಲೇ ಖಾತೆ ಇದೆಯೇ?'},
    'sign_in_here':       {'en': 'Sign in here',       'hi': 'यहां साइन इन करें',       'kn': 'ಇಲ್ಲಿ ಸೈನ್ ಇನ್ ಮಾಡಿ'},
    'pw_mismatch':        {'en': 'Passwords do not match', 'hi': 'पासवर्ड मेल नहीं खाते', 'kn': 'ಪಾಸ್‌ವರ್ಡ್‌ಗಳು ಹೊಂದಾಣಿಕೆಯಾಗುವುದಿಲ್ಲ'},
    'pw_min_placeholder': {'en': 'At least 8 characters', 'hi': 'कम से कम 8 अक्षर', 'kn': 'ಕನಿಷ್ಠ 8 ಅಕ್ಷರಗಳು'},
    'repeat_password':    {'en': 'Repeat your password', 'hi': 'पासवर्ड दोहराएं', 'kn': 'ಪಾಸ್‌ವರ್ಡ್ ಪುನರಾವರ್ತಿಸಿ'},
    'address_placeholder':{'en': 'City, State, PIN code', 'hi': 'शहर, राज्य, पिन कोड', 'kn': 'ನಗರ, ರಾಜ್ಯ, ಪಿನ್ ಕೋಡ್'},

    # ── Browse pages ──
    'needs_title':        {'en': 'Needs from Institutions', 'hi': 'संस्थाओं की जरूरतें', 'kn': 'ಸಂಸ್ಥೆಗಳ ಅಗತ್ಯಗಳು'},
    'needs_subtitle':     {'en': 'Old age homes, orphanages and shelters sharing what they need. Donors can offer to fulfil these.',
                           'hi': 'वृद्धाश्रम, अनाथालय और आश्रय अपनी जरूरतें साझा कर रहे हैं। दानकर्ता इन्हें पूरा करने का प्रस्ताव दे सकते हैं।',
                           'kn': 'ವೃದ್ಧಾಶ್ರಮಗಳು, ಅನಾಥಾಲಯಗಳು ಮತ್ತು ಆಶ್ರಯಗಳು ತಮ್ಮ ಅಗತ್ಯಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತಿವೆ. ದಾನಿಗಳು ಇವುಗಳನ್ನು ಪೂರೈಸಲು ಪ್ರಸ್ತಾವಿಸಬಹುದು.'},
    'no_needs':           {'en': 'No needs posted yet', 'hi': 'अभी कोई जरूरत पोस्ट नहीं', 'kn': 'ಇನ್ನೂ ಯಾವುದೇ ಅಗತ್ಯ ಪೋಸ್ಟ್ ಆಗಿಲ್ಲ'},
    'no_needs_hint':      {'en': 'Institutions will post their needs here.', 'hi': 'संस्थाएं अपनी जरूरतें यहां पोस्ट करेंगी।', 'kn': 'ಸಂಸ್ಥೆಗಳು ತಮ್ಮ ಅಗತ್ಯಗಳನ್ನು ಇಲ್ಲಿ ಪೋಸ್ಟ್ ಮಾಡುತ್ತವೆ.'},
    'items_title':        {'en': 'Available Donated Items', 'hi': 'उपलब्ध दान की वस्तुएं', 'kn': 'ಲಭ್ಯವಿರುವ ದಾನ ವಸ್ತುಗಳು'},
    'items_subtitle':     {'en': 'Browse items donated by our community. Institutions can accept items directly.',
                           'hi': 'हमारे समुदाय द्वारा दान की गई वस्तुएं ब्राउज़ करें। संस्थाएं सीधे वस्तुएं स्वीकार कर सकती हैं।',
                           'kn': 'ನಮ್ಮ ಸಮುದಾಯದಿಂದ ದಾನ ಮಾಡಿದ ವಸ್ತುಗಳನ್ನು ಬ್ರೌಸ್ ಮಾಡಿ. ಸಂಸ್ಥೆಗಳು ನೇರವಾಗಿ ವಸ್ತುಗಳನ್ನು ಸ್ವೀಕರಿಸಬಹುದು.'},
    'no_items':           {'en': 'No items available right now', 'hi': 'अभी कोई वस्तु उपलब्ध नहीं', 'kn': 'ಇപ്പೋ ಯಾವುದೇ ವಸ್ತು ಲಭ್ಯವಿಲ್ಲ'},
    'no_items_hint':      {'en': 'Check back later or donate something.', 'hi': 'बाद में देखें या कुछ दान करें।', 'kn': 'ನಂತರ ಪರಿಶೀಲಿಸಿ ಅಥವಾ ಏನಾದರೂ ದಾನ ಮಾಡಿ.'},
    'quantity':           {'en': 'Quantity',           'hi': 'मात्रा',                  'kn': 'ಪ್ರಮಾಣ'},
    'urgency':            {'en': 'Urgency',            'hi': 'तात्कालिकता',             'kn': 'ತುರ್ತು'},
    'institution':        {'en': 'Institution',        'hi': 'संस्था',                  'kn': 'ಸಂಸ್ಥೆ'},
    'donor':              {'en': 'Donor',              'hi': 'दानकर्ता',                'kn': 'ದಾನಿ'},
    'offer_fulfil':       {'en': 'Offer to Fulfil',    'hi': 'पूरा करने का प्रस्ताव',   'kn': 'ಪೂರೈಸಲು ಪ್ರಸ್ತಾವಿಸಿ'},
    'login_to_offer':     {'en': 'Login to Offer',     'hi': 'प्रस्ताव के लिए लॉग इन',   'kn': 'ಪ್ರಸ್ತಾವಿಸಲು ಲಾಗಿನ್'},
    'only_donors_offer':  {'en': 'Only donors can offer items', 'hi': 'केवल दानकर्ता प्रस्ताव दे सकते हैं', 'kn': 'ದಾನಿಗಳು ಮಾತ್ರ ಪ್ರಸ್ತಾವಿಸಬಹುದು'},
    'accept_item':        {'en': 'Accept Item',        'hi': 'वस्तु स्वीकार करें',      'kn': 'ವಸ್ತು ಸ್ವೀಕರಿಸಿ'},
    'login_to_accept':    {'en': 'Login to Accept',    'hi': 'स्वीकार के लिए लॉग इन',    'kn': 'ಸ್ವೀಕರಿಸಲು ಲಾಗಿನ್'},
    'only_inst_accept':   {'en': 'Only institutions can accept', 'hi': 'केवल संस्थाएं स्वीकार कर सकती हैं', 'kn': 'ಸಂಸ್ಥೆಗಳು ಮಾತ್ರ ಸ್ವೀಕರಿಸಬಹುದು'},

    # ── Status labels ──
    'status_pending':     {'en': 'Pending',            'hi': 'लंबित',                   'kn': 'ಬಾಕಿ'},
    'status_accepted':    {'en': 'Accepted',           'hi': 'स्वीकृत',                 'kn': 'ಸ್ವೀಕರಿಸಲಾಗಿದೆ'},
    'status_completed':   {'en': 'Completed',          'hi': 'पूर्ण',                   'kn': 'ಪೂರ್ಣಗೊಂಡಿದೆ'},

    # ── Error pages ──
    'page_not_found':     {'en': 'Page Not Found',     'hi': 'पृष्ठ नहीं मिला',         'kn': 'ಪುಟ ಕಂಡುಬಂದಿಲ್ಲ'},
    'access_denied':      {'en': 'Access Denied',      'hi': 'पहुंच अस्वीकृत',          'kn': 'ಪ್ರವೇಶ ನಿರಾಕರಿಸಲಾಗಿದೆ'},
    'something_wrong':    {'en': 'Something Went Wrong', 'hi': 'कुछ गलत हो गया',      'kn': 'ಏನೋ ತಪ್ಪಾಗಿದೆ'},
    'back_home':          {'en': '← Back to Home',     'hi': '← होम पर वापस',           'kn': '← ಮುಖಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ'},
    'err_404':            {'en': "Page not found. The page you're looking for doesn't exist.",
                           'hi': 'पृष्ठ नहीं मिला। आप जो पृष्ठ खोज रहे हैं वह मौजूद नहीं है।',
                           'kn': 'ಪುಟ ಕಂಡುಬಂದಿಲ್ಲ. ನೀವು ಹುಡುಕುತ್ತಿರುವ ಪುಟ ಅಸ್ತಿತ್ವದಲ್ಲಿಲ್ಲ.'},
    'err_403':            {'en': "Access denied. You don't have permission to view this page.",
                           'hi': 'पहुंच अस्वीकृत। आपके पास इस पृष्ठ को देखने की अनुमति नहीं है।',
                           'kn': 'ಪ್ರವೇಶ ನಿರಾಕರಿಸಲಾಗಿದೆ. ಈ ಪುಟವನ್ನು ವೀಕ್ಷಿಸಲು ನಿಮಗೆ ಅನುಮತಿ ಇಲ್ಲ.'},
    'err_500':            {'en': 'Something went wrong on our end. Please try again shortly.',
                           'hi': 'हमारी तरफ से कुछ गलत हो गया। कृपया थोड़ी देर में पुनः प्रयास करें।',
                           'kn': 'ನಮ್ಮ ಬದಿಯಿಂದ ಏನೋ ತಪ್ಪಾಗಿದೆ. ದಯವಿಟ್ಟು ಸ್ವಲ್ಪ ಸಮಯದ ನಂತರ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.'},

    # ── Flash / validation messages ──
    'admin_required':     {'en': 'Admin access required.', 'hi': 'व्यवस्थापक पहुंच आवश्यक है।', 'kn': 'ನಿರ್ವಾಹಕ ಪ್ರವೇಶ ಅಗತ್ಯ.'},
    'enter_email_password': {'en': 'Please enter both email and password.', 'hi': 'कृपया ईमेल और पासवर्ड दोनों दर्ज करें।', 'kn': 'ದಯವಿಟ್ಟು ಇಮೇಲ್ ಮತ್ತು ಪಾಸ್‌ವರ್ಡ್ ಎರಡನ್ನೂ ನಮೂದಿಸಿ.'},
    'invalid_email':      {'en': 'Please enter a valid email address.', 'hi': 'कृपया एक मान्य ईमेल पता दर्ज करें।', 'kn': 'ದಯವಿಟ್ಟು ಮಾನ್ಯ ಇಮೇಲ್ ವಿಳಾಸವನ್ನು ನಮೂದಿಸಿ.'},
    'invalid_credentials':{'en': 'Invalid email or password. Please try again.', 'hi': 'अमान्य ईमेल या पासवर्ड। कृपया पुनः प्रयास करें।', 'kn': 'ಅಮಾನ್ಯ ಇಮೇಲ್ ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್. ದಯವಿಟ್ಟು ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.'},
    'err_name_min':       {'en': 'Name must be at least 2 characters.', 'hi': 'नाम कम से कम 2 अक्षर का होना चाहिए।', 'kn': 'ಹೆಸರು ಕನಿಷ್ಠ 2 ಅಕ್ಷರಗಳಾಗಿರಬೇಕು.'},
    'err_password_min':   {'en': 'Password must be at least 8 characters.', 'hi': 'पासवर्ड कम से कम 8 अक्षर का होना चाहिए।', 'kn': 'ಪಾಸ್‌ವರ್ಡ್ ಕನಿಷ್ಠ 8 ಅಕ್ಷರಗಳಾಗಿರಬೇಕು.'},
    'err_role':           {'en': 'Please select a valid role.', 'hi': 'कृपया एक मान्य भूमिका चुनें।', 'kn': 'ದಯವಿಟ್ಟು ಮಾನ್ಯ ಪಾತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ.'},
    'err_phone':          {'en': 'Please enter a valid phone number.', 'hi': 'कृपया एक मान्य फ़ोन नंबर दर्ज करें।', 'kn': 'ದಯವಿಟ್ಟು ಮಾನ್ಯ ಫೋನ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.'},
    'email_registered':   {'en': 'This email is already registered. Please log in.', 'hi': 'यह ईमेल पहले से पंजीकृत है। कृपया लॉग इन करें।', 'kn': 'ಈ ಇಮೇಲ್ ಈಗಾಗಲೇ ನೋಂದಾಯಿಸಲಾಗಿದೆ. ದಯವಿಟ್ಟು ಲಾಗಿನ್ ಮಾಡಿ.'},
    'account_created':    {'en': 'Account created successfully! Please login.', 'hi': 'खाता सफलतापूर्वक बनाया गया! कृपया लॉग इन करें।', 'kn': 'ಖಾತೆ ಯಶಸ್ವಿಯಾಗಿ ರಚಿಸಲಾಗಿದೆ! ದಯವಿಟ್ಟು ಲಾಗಿನ್ ಮಾಡಿ.'},
    'profile_updated':    {'en': 'Profile updated successfully!', 'hi': 'प्रोफ़ाइल सफलतापूर्वक अपडेट!', 'kn': 'ಪ್ರೊಫೈಲ್ ಯಶಸ್ವಿಯಾಗಿ ನವೀಕರಿಸಲಾಗಿದೆ!'},
    'need_posted':        {'en': 'Need posted successfully!', 'hi': 'जरूरत सफलतापूर्वक पोस्ट!', 'kn': 'ಅಗತ್ಯ ಯಶಸ್ವಿಯಾಗಿ ಪೋಸ್ಟ್ ಆಗಿದೆ!'},
    'item_posted':        {'en': 'Item posted successfully!', 'hi': 'वस्तु सफलतापूर्वक पोस्ट!', 'kn': 'ವಸ್ತು ಯಶಸ್ವಿಯಾಗಿ ಪೋಸ್ಟ್ ಆಗಿದೆ!'},
    'only_inst_post_need':{'en': 'Only institutions can post needs.', 'hi': 'केवल संस्थाएं जरूरतें पोस्ट कर सकती हैं।', 'kn': 'ಸಂಸ್ಥೆಗಳು ಮಾತ್ರ ಅಗತ್ಯಗಳನ್ನು ಪೋಸ್ಟ್ ಮಾಡಬಹುದು.'},
    'only_donor_post_item':{'en': 'Only donors can post items.', 'hi': 'केवल दानकर्ता वस्तुएं पोस्ट कर सकते हैं।', 'kn': 'ದಾನಿಗಳು ಮಾತ್ರ ವಸ್ತುಗಳನ್ನು ಪೋಸ್ಟ್ ಮಾಡಬಹುದು.'},
    'only_donor_offer':   {'en': 'Only donors can offer items.', 'hi': 'केवल दानकर्ता प्रस्ताव दे सकते हैं।', 'kn': 'ದಾನಿಗಳು ಮಾತ್ರ ಪ್ರಸ್ತಾವಿಸಬಹುದು.'},
    'need_fulfilled':     {'en': 'This need has already been fulfilled.', 'hi': 'यह जरूरत पहले ही पूरी हो चुकी है।', 'kn': 'ಈ ಅಗತ್ಯ ಈಗಾಗಲೇ ಪೂರೈಸಲಾಗಿದೆ.'},
    'offer_thanks':       {'en': 'Thank you for offering to fulfil this need!', 'hi': 'इस जरूरत को पूरा करने का प्रस्ताव देने के लिए धन्यवाद!', 'kn': 'ಈ ಅಗತ್ಯವನ್ನು ಪೂರೈಸಲು ಪ್ರಸ್ತಾವಿಸಿದ್ದಕ್ಕಾಗಿ ಧನ್ಯವಾದಗಳು!'},
    'only_inst_accept_item':{'en': 'Only institutions can accept items.', 'hi': 'केवल संस्थाएं वस्तुएं स्वीकार कर सकती हैं।', 'kn': 'ಸಂಸ್ಥೆಗಳು ಮಾತ್ರ ವಸ್ತುಗಳನ್ನು ಸ್ವೀಕರಿಸಬಹುದು.'},
    'item_already_accepted':{'en': 'This item has already been accepted.', 'hi': 'यह वस्तु पहले ही स्वीकार की जा चुकी है।', 'kn': 'ಈ ವಸ್ತು ಈಗಾಗಲೇ ಸ್ವೀಕರಿಸಲಾಗಿದೆ.'},
    'item_accepted':      {'en': 'Item accepted successfully!', 'hi': 'वस्तु सफलतापूर्वक स्वीकार!', 'kn': 'ವಸ್ತು ಯಶಸ್ವಿಯಾಗಿ ಸ್ವೀಕರಿಸಲಾಗಿದೆ!'},
    'err_item_name':      {'en': 'Item name must be at least 2 characters.', 'hi': 'वस्तु का नाम कम से कम 2 अक्षर का होना चाहिए।', 'kn': 'ವಸ್ತುವಿನ ಹೆಸರು ಕನಿಷ್ಠ 2 ಅಕ್ಷರಗಳಾಗಿರಬೇಕು.'},
    'err_quantity':       {'en': 'Quantity must be a positive number.', 'hi': 'मात्रा एक धनात्मक संख्या होनी चाहिए।', 'kn': 'ಪ್ರಮಾಣ ಧನಾತ್ಮಕ ಸಂಖ್ಯೆಯಾಗಿರಬೇಕು.'},
    'err_urgency':        {'en': 'Please select a valid urgency level.', 'hi': 'कृपया एक मान्य तात्कालिकता स्तर चुनें।', 'kn': 'ದಯವಿಟ್ಟು ಮಾನ್ಯ ತುರ್ತು ಮಟ್ಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ.'},
    'not_authorised':     {'en': 'You are not authorised to update this donation.', 'hi': 'आप इस दान को अपडेट करने के लिए अधिकृत नहीं हैं।', 'kn': 'ಈ ದಾನವನ್ನು ನವೀಕರಿಸಲು ನಿಮಗೆ ಅಧಿಕಾರವಿಲ್ಲ.'},
    'donation_received':  {'en': 'Donation marked as received. Thank you!', 'hi': 'दान प्राप्त के रूप में चिह्नित। धन्यवाद!', 'kn': 'ದಾನವನ್ನು ಸ್ವೀಕರಿಸಲಾಗಿದೆ ಎಂದು ಗುರುತಿಸಲಾಗಿದೆ. ಧನ್ಯವಾದಗಳು!'},
    'status_updated':     {'en': 'Status updated to {status}.', 'hi': 'स्थिति {status} में अपडेट।', 'kn': 'ಸ್ಥಿತಿಯನ್ನು {status} ಗೆ ನವೀಕರಿಸಲಾಗಿದೆ.'},
    'donation_marked':    {'en': 'Donation marked as {status}.', 'hi': 'दान {status} के रूप में चिह्नित।', 'kn': 'ದಾನವನ್ನು {status} ಎಂದು ಗುರುತಿಸಲಾಗಿದೆ.'},
}
# fmt: on

STATUS_MAP = {
    'Pending': 'status_pending',
    'Accepted': 'status_accepted',
    'Completed': 'status_completed',
}


def _lang():
    lang = session.get('lang', 'en')
    return lang if lang in SUPPORTED else 'en'


def t(key, **kwargs):
    """Translate a string key for the current session language."""
    lang = _lang()
    entry = TRANSLATIONS.get(key, {})
    text = entry.get(lang) or entry.get('en') or key
    if kwargs:
        return text.format(**kwargs)
    return text


def t_status(status):
    """Translate a database status value."""
    key = STATUS_MAP.get(status)
    return t(key) if key else status
