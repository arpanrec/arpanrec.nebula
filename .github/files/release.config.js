module.exports = {
    branches: ["main"],
    tagFormat: "${version}",
    plugins: [
        [
            "@semantic-release/commit-analyzer",
            {
                preset: "angular",
                parserOpts: {
                    noteKeywords: [
                        "BREAKING CHANGE",
                        "BREAKING CHANGES",
                        "BREAKING",
                    ],
                },
            },
        ],
        [
            "@semantic-release/release-notes-generator",
            {
                preset: "angular",
                parserOpts: {
                    noteKeywords: [
                        "BREAKING CHANGE",
                        "BREAKING CHANGES",
                        "BREAKING",
                    ],
                },
                writerOpts: {
                    commitsSort: ["subject", "scope"],
                },
            },
        ],
        [
            "@semantic-release/changelog",
            {
                changelogFile: "CHANGELOG.md",
            },
        ],
        [
            "@semantic-release/exec",
            {
                prepareCmd:
                    "sed -i 's/^version:.*/version: ${nextRelease.version}/g' galaxy.yml && poetry export --without-hashes --format=requirements.txt --with dev > .github/files/requirements.txt && poetry version ${nextRelease.version}", //&& ansible-galaxy collection build",
                successCmd:
                    "git checkout -b release/${nextRelease.version} && git push --set-upstream origin release/${nextRelease.version}",
            },
        ],
        [
            "@semantic-release/git",
            {
                assets: [
                    "galaxy.yml",
                    "CHANGELOG.md",
                    ".github/files/requirements.txt",
                    "pyproject.toml",
                ],
                message:
                    "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
            },
        ],
        [
            "@semantic-release/github",
            {
                // assets: [
                //   {
                //     path: "arpanrec-nebula-*.tar.gz",
                //     label: "Collection tarball",
                //   },
                // ],
            },
        ],
    ],
};
