Skip to content
Search
Pulls
Issues
Marketplace
Explore
 
@legendarmy12 
LEGENDXOP
/
LEGEND-BOT
2
28114
Code
Issues
Pull requests
1
Discussions
Actions
Projects
Wiki
Security
Insights
LEGEND-BOT/.github/workflows/ok.yml
@LEGENDXOP
LEGENDXOP Create ok.yml
Latest commit a334dc6 on 13 Mar
 History
 1 contributor
40 lines (20 sloc)  603 Bytes
 

name: LEGENDX

on: push

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v2

      - name: Find and Replace

        uses: jacobtomlinson/gha-find-replace@master

        with:

          find: "MASTERBOT"

          replace: "LEGEND_ARMY_BOT"

      - name: Create Pull Request

        uses: stefanzweifel/git-auto-commit-action@v4

        with:

          commit_message: 'Replaced new name'

          commit_options: '--no-verify'

          repository: .

          commit_user_name: LEGENDXOP

          commit_user_email: legendxx08377@gmail.com
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
