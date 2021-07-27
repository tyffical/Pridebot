# Contributing to this repository 

## Getting started 

Before you begin:
- This bot is powered by Discord.py
- Check out the [existing issues](https://github.com/tyffical/Pridebot/issues) & see if we accept contributions


### Don't see your issue? Open one

If you spot something new, open an issue using a [template](https://github.com/tyffical/Pridebot/issues/new). We'll use the issue to have a conversation about the problem you want to fix.

### Ready to make a change? Fork the repo

Fork using GitHub Desktop:

- [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) will guide you through setting up Desktop.
- Once Desktop is set up, you can use it to [fork the repo](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop)!

Fork using the command line:

- [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.
Fork using Githubs fork button:

Fork using the Github Fork button:

- click on the Fork button at to top right coner 


### Make your update:
Make your changes to the file(s) you'd like to update.
  - Are you making changes to the application code? You'll need **discord.py** to run the bot locally. See [contributing/development.md](contributing/development.md).
  - Are you contributing to markdown? We use [GitHub Markdown](contributing/content-markup-reference.md).

### Open a pull request
When you're done making changes and you'd like to propose them for review, use the [pull request template](#pull-request-template) to open your PR (pull request).or make your own

### Submit your PR & get it reviewed
- Once you submit your PR, others Contributors  will review it with you.
- After that, we may have questions, check back on your PR to keep up with the conversation.
- Did you have an issue, like a merge conflict? Check out our [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) on how to resolve merge conflicts and other issues.

### Your PR is merged!
Congratulations! The whole GitHub community thanks you. :sparkles:

Once your PR is merged, you will be proudly listed as a contributor in the [contributor chart](https://github.com/tyffical/Pridebot/graphs/contributors).

### Keep contributing as you use GitHub Docs

Now that you're a part of the GitHub Docs community, you can keep participating in many ways.

**Learn more about contributing:**

- [Types of contributions :memo:](#types-of-contributions-memo)
  - [:mega: Discussions](#mega-discussions)
  - [:beetle: Issues](#beetle-issues)
  - [:hammer_and_wrench: Pull requests](#hammer_and_wrench-pull-requests)
  - [:question: Support](#question-support)
  - [:earth_asia: Translations](#earth_asia-translations)
  - [:balance_scale: Site Policy](#balance_scale-site-policy)
- [Starting with an issue](#starting-with-an-issue)
  - [Labels](#labels)
- [Opening a pull request](#opening-a-pull-request)
- [Working in the github/docs repository](#working-in-the-githubdocs-repository)
- [Reviewing](#reviewing)
  - [Self review](#self-review)
  - [Pull request template](#pull-request-template)
  - [Suggested changes](#suggested-changes)
- [Windows](#windows)

## Types of contributions :memo:
You can contribute to the GitHub Docs content and site in several ways. This repo is a place to discuss and collaborate on docs.github.com! Our small, but mighty :muscle: docs team is maintaining this repo, to preserve our bandwidth, off topic conversations will be closed.

### :mega: Discussions
Discussions are where we have conversations.

If you'd like help troubleshooting a docs PR you're working on, have a great new idea, or want to share something amazing you've learned in our docs, join us in [discord](https://blahajgang.lol/).

### :beetle: Issues
[Issues](https://docs.github.com/en/github/managing-your-work-on-github/about-issues) are used to track tasks that contributors can help with. If an issue has a triage label, we haven't reviewed it yet and you shouldn't begin work on it.

If you've found something in the content or the website that should be updated, search open issues to see if someone else has reported the same thing. If it's something new, open an issue using a [template](https://github.com/tyffical/Pridebot/issues/new/choose). We'll use the issue to have a conversation about the problem you want to fix.

### :hammer_and_wrench: Pull requests
A [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) is a way to suggest changes in our repository.

When we merge those changes, they should be deployed to the live site within 24 hours. :earth_africa: To learn more about opening a pull request in this repo, see [Opening a pull request](#opening-a-pull-request) below.

### :question: Support
We are a small team working hard to keep up with the documentation demands of a continuously changing product. Unfortunately, we just can't help with support questions in this repository. If you are experiencing a problem with GitHub, unrelated to our documentation, please [contact GitHub Support directly](https://support.github.com/contact). Any issues, discussions, or pull requests opened here requesting support will be given information about how to contact GitHub Support, then closed and locked.

If you're having trouble with your GitHub account, contact [Support](https://support.github.com/contact).


## Starting with an issue
You can browse existing issues to find something that needs help!

### Labels
Labels can help you find an issue you'd like to help with.
- The [`help wanted` label](https://github.com/github/docs/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) is for problems or updates that anyone in the community can start working on.
- The [`good first issue` label](https://github.com/github/docs/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) is for problems or updates we think are ideal for beginners.
- The [`content` label](https://github.com/github/docs/issues?q=is%3Aopen+is%3Aissue+label%3Acontent) is for problems or updates in the content on docs.github.com. These will usually require some knowledge of Markdown.
- The [`engineering` label](https://github.com/github/docs/issues?q=is%3Aopen+is%3Aissue+label%3Aengineering) is for problems or updates in the docs.github.com website. These will usually require some knowledge of JavaScript/Node.js or YAML to fix.

## Opening a pull request
You can use the GitHub user interface :pencil2: for some small changes, like fixing a typo or updating a readme. You can also fork the repo and then clone it locally, to view changes and run your tests on your machine.


### Self review
You should always review your own PR first.

For content changes, make sure that you:
- [ ] Confirm that the changes meet the user experience and goals outlined in the content design plan (if there is one).
- [ ] Compare your pull request's source changes to staging to confirm that the output matches the source and that everything is rendering as expected. This helps spot issues like typos, content that doesn't follow the style guide, or content that isn't rendering due to versioning problems. Remember that lists and tables can be tricky.
- [ ] Review the content for technical accuracy.
- [ ] Review the entire pull request using the [localization checklist](contributing/localization-checklist.md).
- [ ] Copy-edit the changes for grammar, spelling, and adherence to the [style guide](https://github.com/github/docs/blob/main/contributing/content-style-guide.md).
- [ ] Check new or updated Liquid statements to confirm that versioning is correct.
- [ ] If there are any failing checks in your PR, troubleshoot them until they're all passing.

### Pull request template
When you open a pull request, you must fill out the "Ready for review" template before we can review your PR. This template helps reviewers understand your changes and the purpose of your pull request.

### Suggested changes
We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.

As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).

