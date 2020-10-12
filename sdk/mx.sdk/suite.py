#
# Copyright (c) 2018, 2019, Oracle and/or its affiliates. All rights reserved.
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# The Universal Permissive License (UPL), Version 1.0
#
# Subject to the condition set forth below, permission is hereby granted to any
# person obtaining a copy of this software, associated documentation and/or
# data (collectively the "Software"), free of charge and under any and all
# copyright rights in the Software, and any and all patent rights owned or
# freely licensable by each licensor hereunder covering either (i) the
# unmodified Software as contributed to or provided by such licensor, or (ii)
# the Larger Works (as defined below), to deal in both
#
# (a) the Software, and
#
# (b) any piece of software and/or hardware listed in the lrgrwrks.txt file if
# one is included with the Software each a "Larger Work" to which the Software
# is contributed by such licensors),
#
# without restriction, including without limitation the rights to copy, create
# derivative works of, display, perform, and distribute the Software and make,
# use, sell, offer for sale, import, export, have made, and have sold the
# Software and the Larger Work(s), and to sublicense the foregoing rights on
# either these or other terms.
#
# This license is subject to the following condition:
#
# The above copyright notice and either this complete permission notice or at a
# minimum a reference to the UPL must be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
suite = {
  "mxversion" : "5.251.0",
  "name" : "sdk",
  "version" : "20.2.0.0",
  "release" : True,
  "sourceinprojectwhitelist" : [],
  "url" : "https://github.com/oracle/graal",
  "groupId" : "org.graalvm.sdk",
  "developer" : {
    "name" : "GraalVM Development",
    "email" : "graalvm-dev@oss.oracle.com",
    "organization" : "Oracle Corporation",
    "organizationUrl" : "http://www.graalvm.org/",
  },
  "scm" : {
    "url" : "https://github.com/oracle/graal",
    "read" : "https://github.com/oracle/graal.git",
    "write" : "git@github.com:oracle/graal.git",
  },
  "repositories" : {
    "lafo-snapshots" : {
      "url" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots",
      "licenses" : ["GPLv2-CPE", "UPL", "BSD-new", "NCSA"]
    },
    "lafo" : {
      "snapshotsUrl" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots",
      "releasesUrl": "https://curio.ssw.jku.at/nexus/content/repositories/releases",
      "licenses" : ["GPLv2-CPE", "UPL", "BSD-new", "MIT", "NCSA"],
    },
    "lafo-maven" : {
      "snapshotsUrl" : "https://curio.ssw.jku.at/nexus/content/repositories/maven-snapshots",
      "releasesUrl": "https://curio.ssw.jku.at/nexus/content/repositories/maven-releases",
      "licenses" : ["GPLv2-CPE", "UPL", "BSD-new", "MIT", "NCSA"],
      "mavenId" : "lafo",
    },
  },
  "snippetsPattern" : ".*(Snippets|doc-files).*",
  "defaultLicense" : "UPL",
  "imports": {},
  "libraries" : {
    "JLINE" : {
      "sha1" : "c3aeac59c022bdc497c8c48ed86fa50450e4896a",
      "maven" : {
        "groupId" : "jline",
        "artifactId" : "jline",
        "version" : "2.14.6",
      },
      "license" : "BSD-new"
    },
    "LLVM_ORG" : {
      "version" : "9.0.0-5-g80b1d876fd-bgb66b241662",
      "os_arch" : {
        "linux" : {
          "amd64" : {
            "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/llvm-org/llvm-llvmorg-{version}-linux-amd64.tar.gz"],
            "sha1" : "7fd347a6ebe38b02b7cfe1a9e4352e297962a4fc",
          },
          "aarch64" : {
            "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/llvm-org/llvm-llvmorg-{version}-linux-aarch64.tar.gz"],
            "sha1" : "8061112dd5cf95ed5e43128199fd2d2959bd9fbf",
          }
        },
        "darwin" : {
          "amd64" : {
            "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/llvm-org/llvm-llvmorg-{version}-darwin-amd64.tar.gz"],
            "sha1" : "a863230a50eddeef4a808742ddb987475c61fd10",
          }
        },
        "<others>": {
            "<others>": {
                "optional": True,
            }
        },
        "license" : "Apache-2.0-LLVM",
      }
    },
    "LLVM_ORG_COMPILER_RT_LINUX" : {
      "version" : "9.0.0-5-g80b1d876fd-bgb66b241662",
      # we really want linux-amd64, also on non-linux and non-amd64 platforms for cross-compilation
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/llvm-org/compiler-rt-llvmorg-{version}-linux-amd64.tar.gz"],
      "sha1" : "0fde45454791eff6b1cd1dbed21645ebe073c0d2",
      "license" : "Apache-2.0-LLVM",
    },
    "LLVM_ORG_SRC" : {
      # version difference since the sources where repackaged
      "version" : "9.0.0-5-g80b1d876fd-bg0c808efbe5",
      "packedResource" : True,
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/llvm-org/llvm-src-llvmorg-{version}.tar.gz"],
      "sha1" : "27bea70346768ee43893df3f65cf785c5b5d0342",
      "license" : "Apache-2.0-LLVM",
      },
  },
  "projects" : {
    "org.graalvm.options" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK",
    },
    "org.graalvm.polyglot" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.collections",
        "org.graalvm.home",
      ],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK",
    },

    "org.graalvm.word" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "checkstyleVersion" : "8.8",
      "workingSets" : "API,SDK",
    },

    "org.graalvm.nativeimage" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.word",
        "org.graalvm.options",
      ],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK",
    },
    "org.graalvm.nativeimage.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.nativeimage"
      ],
      "javaCompliance" : "8+",
      "workingSets" : "SDK",
      "checkstyle" : "org.graalvm.word",
    },
    "org.graalvm.launcher" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.polyglot",
        "JLINE",
      ],
      "javaCompliance" : "8+",
      "workingSets" : "Truffle,Tools",
      "checkstyle" : "org.graalvm.word",
    },
    "org.graalvm.launcher.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.launcher"
      ],
      "javaCompliance" : "8+",
      "workingSets" : "Truffle,Tools,Test",
      "checkstyle" : "org.graalvm.word",
    },
    "org.graalvm.polyglot.tck" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.polyglot",
      ],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK,Test",
    },
    "org.graalvm.collections" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK",
    },
    "org.graalvm.collections.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.collections",
      ],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK,Test",
    },
    "org.graalvm.home" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "org.graalvm.nativeimage",
      ],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK",
    },
    "org.graalvm.home.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "mx:JUNIT",
        "org.graalvm.home",
      ],
      "checkstyle" : "org.graalvm.word",
      "javaCompliance" : "8+",
      "workingSets" : "API,SDK",
    },
  },
  "licenses" : {
    "UPL" : {
      "name" : "Universal Permissive License, Version 1.0",
      "url" : "http://opensource.org/licenses/UPL",
    },
    "NCSA" : {
      "name" : "University of Illinois/NCSA Open Source License",
      "url" : "https://releases.llvm.org/8.0.0/LICENSE.TXT"
    },
    "Apache-2.0-LLVM" : {
      "name" : "Apache License 2.0 with LLVM Exceptions",
      "url" : "http://releases.llvm.org/9.0.0/LICENSE.TXT"
    },
},

  # ------------- Distributions -------------
  "distributions" : {
    "GRAAL_SDK" : {
      "subDir" : "src",
      "dependencies" : [
        "org.graalvm.polyglot",
        "org.graalvm.nativeimage",
        "org.graalvm.collections",
        "org.graalvm.home",
      ],
      "distDependencies" : [],
      "javadocType": "api",
      "moduleInfo" : {
        "name" : "org.graalvm.sdk",
        "requires" : ["java.logging"],
        "exports" : [
          "org.graalvm.collections",
          "org.graalvm.home",
          "org.graalvm.home.impl",
          "org.graalvm.nativeimage.hosted",
          "org.graalvm.nativeimage.c.function",
          "org.graalvm.nativeimage.c.struct",
          "org.graalvm.nativeimage.c.type",
          "org.graalvm.nativeimage.c.constant",
          "org.graalvm.nativeimage.c",
          "org.graalvm.nativeimage",
          "org.graalvm.nativeimage.impl.clinit", # class initialization instrumentation
          "org.graalvm.polyglot.proxy",
          "org.graalvm.polyglot.io",
          "org.graalvm.polyglot.management",
          "org.graalvm.polyglot",
          "org.graalvm.options",
          "org.graalvm.word",
          "org.graalvm.polyglot.impl to org.graalvm.truffle",
          "org.graalvm.word.impl to jdk.internal.vm.compiler",
        ],
        "uses" : [
          "org.graalvm.polyglot.impl.AbstractPolyglotImpl"
        ],
      },
      "description" : "GraalVM is an ecosystem for compiling and running applications written in multiple languages.\nGraalVM removes the isolation between programming languages and enables interoperability in a shared runtime.",
    },
    "SDK_TEST" : {
      "subDir" : "src",
      "dependencies" : [
        "org.graalvm.collections.test",
        "org.graalvm.nativeimage.test",
        "org.graalvm.launcher.test",
        "org.graalvm.home.test",
      ],
      "distDependencies" : [
        "GRAAL_SDK",
        "LAUNCHER_COMMON"
      ],
      "maven" : False,
    },
    "LAUNCHER_COMMON" : {
      "subDir" : "src",
      "moduleInfo" : {
        "name" : "org.graalvm.launcher",
      },
      "dependencies" : [
        "org.graalvm.launcher",
      ],
      "distDependencies" : [
        "GRAAL_SDK",
      ],
      "description" : "Common infrastructure to create language launchers using the Polyglot API.",
      "allowsJavadocWarnings": True,
    },
    "POLYGLOT_TCK" : {
      "subDir" : "src",
      "moduleInfo" : {
        "name" : "org.graalvm.polyglot_tck",
        "exports" : [
          "org.graalvm.polyglot.tck"
        ],
      },
      "dependencies" : [
        "org.graalvm.polyglot.tck",
      ],
      "distDependencies" : [
        "GRAAL_SDK",
      ],
      "javadocType": "api",
      "description" : """GraalVM TCK SPI""",
    },
    "LLVM_TOOLCHAIN": {
      "native": True,
      "description": "LLVM with general purpose patches used by Sulong and Native Image",
      "layout": {
        "./": [
          "extracted-dependency:LLVM_ORG",
          "extracted-dependency:LLVM_ORG_COMPILER_RT_LINUX",
          "file:3rd_party_license_llvm-toolchain.txt",
        ],
        "./patches/" : [
          "file:patches/*",
        ],
        "./patches/graalvm-llvm-runtime/" : [
          "file:../sulong/patches/*",
        ],
        "./patches/native-image/" : [
          "file:../substratevm/patches/*"
        ],
      },
      "platformDependent" : True,
      "maven": False,
      "license" : "Apache-2.0-LLVM",
    },
  },
}
