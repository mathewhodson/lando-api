# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# yapf: disable
CANNED_USERINFO_1 = {
    'sub': 'ad|Example-LDAP|testuser',
    'name': 'Test User',
    'given_name': 'Test',
    'family_name': 'User',
    'nickname': 'Test User',
    'picture': 'https://s.gravatar.com/avatar/7ec7606c46a14a7ef514d1f1f9038823?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Ftu.png',
    'updated_at': '2017-10-24T13:15:12.120Z',
    'https://sso.mozilla.com/claim/groups': [
        'active_scm_level_1',
        'all_scm_level_1',
        'active_scm_level_3',
        'all_scm_level_3',
        'active_scm_level_2',
        'all_scm_level_2',
    ],
    'https://sso.mozilla.com/claim/emails': [
        'tuser@example.com',
        'test@example.com',
    ],
    'https://sso.mozilla.com/claim/dn': 'mail=tuser@example.com,o=com,dc=example',
    'https://sso.mozilla.com/claim/organizationUnits': 'mail=tuser@example.com,o=com,dc=example',
    'https://sso.mozilla.com/claim/email_aliases': 'test@example.com',
    'https://sso.mozilla.com/claim/_HRData': {
        'placeholder': 'empty',
    },
}
