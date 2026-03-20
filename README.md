# Resumescence

Resumescence is an app that makes it easy to write and iterate on resumes.
It does this by offering users the ability to write latex components.

## High-level usage
All resumes or latex documents that are distinct from one another are separated into Projects.
Each project contains multiple features:
1) Definitions
	- Latex file where a user can set up custom definitions
 2) Components
	 - A document is a file, like a resume.
	 - When a document is edited, it is either overwritten or saved as a copy
		 - this allows for quick iteration

## Components

#### Editing a Component
A component is itself just latex code that can be edited in a builtin code editor. This code can be edited normally. However, it also may contain components. These components will have their code shown, in a collapsible form, in a way that makes it clear that this code is uneditable as it comes from a different component. By clicking on the component area, you open the editor for that specific component. You can also open up a right hand side panel that provides a rendered preview of all components and can be drag-and-dropped into the editing panel.

#### Viewing a rendered component
Ctrl + G to swap between code-view and rendered view, or alternatively go for a splitscreen version, which may make things cluttered.

#### Organization
To keep things organized, components that are opened/closed are available in a row of tabs in the top, and can be quickly navigated via ctrl-tab and ctrl-shift-tab.

#### Creating new Components
A new component can be added in the left sidebar with a + icon. Alternatively, a section of code can be highlighted, and given that it is compilable, it can be converted into a new component.

## GUI
Obsidian has a good setup. 
Top left contains project select.
Left sidebar for components.
Middle area for code editing, with functionality for splitscreen with live latex compilation.
Right sidebar with rendered component dropdown.
Top bar with tabs

## Implementation (Phase 1)
Local Electron App to be used personally to iron out issues and mold it to perfection. During development, I need to structure it in such a way that in the future it will be as easy as possible to reuse code and attach it to a backend.

#### Tech Stack
1) Electron - graphical interface
2) Python - backend
3) SQLite - database

## Notes
- displaying errors
- iterating on documents, saving versions