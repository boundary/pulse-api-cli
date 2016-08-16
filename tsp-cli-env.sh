#
# Copyright 2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

export BOUNDARY_API_SHELL_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
#typeset -r CONFIG_DIR=".ts_pulse"
CONFIG_DIR=".ts_pulse"

#
# Shows the current environment
#
function tsp-env() {
env | egrep '(BOUNDARY|TSI|TSP)' | sort
}

#
# List the currently configured environments
#
function tsp-list() {
  local count=1
  for config in $(ls -1 "$HOME/$CONFIG_DIR/accounts")
  do
    printf "%s) %s\n" "$count" "$config"
    count=$((count + 1))
  done
}

#
# Change the environment
#
function tsp-set() {
  typeset config=$1
  typeset -i rc=0

  # Create a menu if a configuration was not specified
  if [ -z "$config" ]
  then
    select opt in $(ls -1 $HOME/$CONFIG_DIR/accounts); do
      config="$opt"
      break
    done
  fi

  #
  # If the configuration exists then source it
  #
  if [ -r "$HOME/$CONFIG_DIR/accounts/$config" ]
  then
    source "$HOME/$CONFIG_DIR/accounts/$config"
    rc=0
  else
    rc=1
  fi

  #
  # Output the current environment
  #
  tsp-env
  return $rc
}

#
# Configure completion
#
if [ -r $HOME/.boundary/accounts ]
then
  complete -o filenames -W "$(cd $HOME/$CONFIG_DIR/accounts ; ls -1)" tsp-set
fi

