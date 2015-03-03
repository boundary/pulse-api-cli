###
### Copyright 2014, Boundary
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###     http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
###

export BOUNDARY_API_SHELL_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/account"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/actions"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/events"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/meter"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/metrics"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/plugins"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/relays"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/sources"
export PATH="$PATH:$BOUNDARY_API_SHELL_HOME/src/main/scripts/user"

alias bsenv="env | grep BOUNDARY | sort"

#
# Shows the current environment
#
function bp-env() {
  env | grep BOUNDARY | sort
}

#
# List the currently configured environments
#
function bp-acc() {
  local count=1
  for config in $(ls -1 "$HOME/.boundary/accounts")
  do
    printf "%s) %s\n" "$count" "$config"
    count=$((count + 1))
  done
}

#
# Change the environment
#
function bp-set() {
  typeset config=$1
  typeset -i rc=0

  # Create a menu if a configuration was not specified
  if [ -z "$config" ]
  then
    select opt in $(ls -1 $HOME/.boundary/accounts); do
      config="$opt"
      break
    done
  fi

  #
  # If the configuration exists then source it
  #
  if [ -r "$HOME/.boundary/accounts/$config" ]
  then
    source "$HOME/.boundary/accounts/$config"
    rc=0
  else
    rc=1
  fi

  bp-env
  return $rc
}

#
# Configure completion
#
if [ -r $HOME/.boundary/accounts ]
then
  complete -o filenames -W "$(cd $HOME/.boundary/accounts ; ls -1)" bp-set
fi

