require "minitest"
require "minitest/autorun"
require "minitest/reporters"
require "minitest/skip_dsl"


Minitest::Reporters.use! Minitest::Reporters::SpecReporter.new

require_relative "../lib/linked_list.rb"
require_relative "../lib/queue.rb"
require_relative "../lib/stack.rb"
require_relative "../lib/problems.rb"