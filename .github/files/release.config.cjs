module.exports = {
    branches: ['main'],
    tagFormat: '${version}',
    plugins: [
        [
            '@semantic-release/commit-analyzer',
            {
                preset: 'angular',
                parserOpts: {
                    noteKeywords: ['BREAKING CHANGE', 'BREAKING CHANGES', 'BREAKING'],
                },
            },
        ],
        [
            '@semantic-release/release-notes-generator',
            {
                preset: 'angular',
                parserOpts: {
                    noteKeywords: ['BREAKING CHANGE', 'BREAKING CHANGES', 'BREAKING'],
                },
                writerOpts: {
                    commitsSort: ['subject', 'scope'],
                },
            },
        ],
        [
            '@semantic-release/changelog',
            {
                changelogFile: 'CHANGELOG.md',
            },
        ],
        [
            '@semantic-release/exec',
            {
                prepareCmd:
                    "sed -i 's/^version:.*/version: ${nextRelease.version}/g' galaxy.yml && poetry export --without-hashes --format=requirements.txt --with dev > .github/files/requirements.txt && poetry version ${nextRelease.version} && poetry lock && ansible-galaxy collection build",
                successCmd:
                    'ansible-galaxy collection publish arpanrec-nebula-${nextRelease.version}.tar.gz --api-key ${process.env.GALAXY_API_KEY}',
            },
        ],
        [
            '@semantic-release/git',
            {
                assets: [
                    'galaxy.yml',
                    'poetry.lock',
                    'CHANGELOG.md',
                    '.github/files/requirements.txt',
                    'pyproject.toml',
                ],
                message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}',
            },
        ],
        // [
        //     '@semantic-release/github',
        //     {
        //         assets: [
        //           {
        //             path: "arpanrec-nebula-*.tar.gz",
        //             label: "Collection tarball",
        //           },
        //         ],
        //     },
        // ],
    ],
};
